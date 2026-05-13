# Python fundamentals — lessons learned while debugging romanNumeralConverter.py
# =============================================================================


# 1. `python -c` basics
# ---------------------
# - Runs inline Python code directly from the terminal, no file needed.
# - The `-c` stands for "command".
# - Top-level code cannot have leading whitespace.
#   Even 2 spaces before `print(...)` on a new line => IndentationError.
# - Example (works):
#     python -c "print('hi')"
# - Example (fails):
#     python -c "print('hi');
#       print('bye')"         # <- leading spaces = error


# 2. Imports use the module name, not the filename
# ------------------------------------------------
# - Correct:   from romanNumeralConverter import convertRomanNumeralToInteger
# - Wrong:     from romanNumeralConverter.py import convertRomanNumeralToInteger
# - Wrong:     from romanNumeralConverter.py.py import ...
# - Rule: drop the `.py` extension when importing.


# 3. Type annotations — name first, then `:`, then type
# -----------------------------------------------------
# - Correct:   def f(romanNumeral: str) -> int:
# - Wrong:     def f(string romanNumeral) -> int:   # Java-style, not Python
# - Wrong:     def f(string: romanNumeral) -> int:  # name and type swapped
# - Rule: parameter NAME comes first, then `:`, then the TYPE.
# - Common types: str, int, float, bool, list, dict, tuple.


# 4. Indentation must be consistent
# ---------------------------------
# - All statements at the same block level must use the same indent.
# - Deeper indent is only allowed after a line ending with `:`
#   (def, if, for, while, class, etc.).
# - Python convention: 4 spaces per level.
# - Correct:
#     def f(x):
#         total = 0
#         for c in x:
#             total += 1
#         return total
# - Wrong (mixed 2/4/6 spaces at the same level):
#     def f(x):
#       total = 0
#         for c in x:           # <- "unexpected indent"
#           total += 1
#         return total


# 5. Python is case-sensitive
# ---------------------------
# - `romanChar` and `RomanChar` are two different names.
# - If you define `for romanChar in ...` and then use `values[RomanChar]`,
#   you get `NameError: name 'RomanChar' is not defined`.
# - Rule: names must match exactly, including capitalization.


# 6. `for char in string` vs `for i in range(len(string))`
# --------------------------------------------------------
# - `for char in "XIV":` gives you each character, but no way to peek ahead.
# - `for i in range(len("XIV")):` gives you the index (0, 1, 2),
#   so you can access string[i] AND string[i+1] (look-ahead).
# - Use range(len(...)) when you need to compare adjacent elements.


# 7. `range(n)` goes from 0 to n-1, not n
# ----------------------------------------
# - range(3) = 0, 1, 2
# - len("XIV") = 3, valid indices = 0, 1, 2
# - So range(len(s)) produces exactly the valid indices.
# - Use `i+1 < len(s)` (not `<=`) to check if a next element exists.


# 8. Python has no `i++`
# ----------------------
# - Use `i += 1` instead.
# - Also: `i += 1` inside a `for i in range(...)` loop has NO EFFECT
#   on the next iteration — the for loop controls `i`, not you.
# - If you need to skip indices, use a `while` loop instead.


# 9. Each `else` belongs to its nearest `if` at the same indent
# -------------------------------------------------------------
# - You cannot make an `else` "jump" to a different `if`.
# - Python matches if/else strictly by indentation level.
# - If you have nested ifs, each needs its own else if needed.


# 10. Python integers can be negative
# ------------------------------------
# - `totalSum -= 1` is valid even if totalSum is 0 (result = -1).
# - Useful for the look-ahead subtraction pattern in Roman numerals:
#   "IV" → subtract I(1), then add V(5) → total = -1 + 5 = 4.
# - Intermediate negative values are fine — the final result is correct.


# 11. `sys.argv` — command-line arguments
# ----------------------------------------
# - `sys.argv` is a list of strings from the command line.
# - sys.argv[0] = the script name (always present)
# - sys.argv[1] = first argument, sys.argv[2] = second, etc.
# - Example: `python romanNumeralConverter.py XIV`
#     sys.argv[0] = "romanNumeralConverter.py"
#     sys.argv[1] = "XIV"
# - Requires `import sys` at the top of the file.


# 12. `if __name__ == "__main__":` guard
# --------------------------------------
# - Runs the block only when the file is executed directly:
#     python myfile.py         → __name__ is "__main__"  → runs
#     from myfile import func  → __name__ is "myfile"    → skipped
# - Without this guard, the code runs on import too (e.g. in tests).
# - Standard pattern for CLI entry points:
#     if __name__ == "__main__":
#         print(myFunction(sys.argv[1]))


# 13. `for pattern in list` + `if pattern in string`
# ---------------------------------------------------
# - `in` does two different things depending on context:
#     for x in myList:       → iterates through the list
#     if "IV" in "XIVIII":   → checks if substring exists
# - Useful for validation: loop through bad patterns, check each one.
# - Example:
#     invalidPatterns = ["IIII", "VV", "IL"]
#     for pattern in invalidPatterns:
#         if pattern in romanNumeral:
#             raise ValueError(f"Invalid: contains '{pattern}'")


# 14. Unit tests live in a separate file
# ---------------------------------------
# - Convention: test_<module>.py next to the module it tests.
# - pytest auto-discovers files matching `test_*.py` or `*_test.py`.
# - Each test function name must start with `test_`.
# - Run with `pytest` from the folder (no arguments needed).


# 15. One concept per test
# ------------------------
# - Each test checks ONE behavior. Don't bundle unrelated assertions.
# - If a test fails, the name should tell you what broke.
# - Good:  test_IX_converts_to_9
# - Bad:   test_conversion_works  (too vague — what exactly?)


# 16. Arrange-Act-Assert (AAA) pattern
# -------------------------------------
# - Structure each test in 3 visible steps:
#     input = "III"                                    # arrange
#     result = convertRomanNumeralToInteger(input)     # act
#     assert result == 3                               # assert
# - For trivial tests, collapse into one line:
#     def test_III_is_3(): assert convertRomanNumeralToInteger("III") == 3


# 17. Test names should read like a spec
# ---------------------------------------
# - Format: test_<input>_<expected behavior>
# - Examples:
#     test_I_is_1
#     test_IIII_is_rejected
#     test_empty_string_raises_error
# - Someone reading only the test names should understand what the code does.


# 18. Test both happy path AND error cases
# -----------------------------------------
# - Don't just test valid inputs. Test that invalid inputs fail correctly.
# - Use `pytest.raises(ExceptionType)` to assert an exception is raised:
#     def test_IIII_is_rejected():
#         with pytest.raises(ValueError):
#             convertRomanNumeralToInteger("IIII")


# 19. Running pytest
# ------------------
# - `pytest`                       → runs all test files in the folder
# - `pytest test_file.py`          → runs one file
# - `pytest -v`                    → verbose (shows each test name)
# - `pytest -k "subtractive"`      → runs tests with keyword in name
# - `pytest file.py::test_func`    → runs a single test function


# 20. Pure functions — the two rules
# -----------------------------------
# A function is "pure" if it satisfies BOTH:
#   (a) Same input → same output (deterministic, no hidden dependencies)
#   (b) No side effects (doesn't modify anything outside itself)
#
# Side effects include: printing, reading/writing files, network calls,
# mutating global state, mutating input arguments, reading the clock, etc.
#
# - Pure:    def add(a, b): return a + b
# - Impure:  def greet(name): return f"hi {name} at {datetime.now()}"  # clock
# - Impure:  def addItem(lst, x): lst.append(x); return lst            # mutates input


# 21. Why purity matters in practice
# -----------------------------------
# - Easier to test: give input, check output. No mocks, no setup.
# - Easier to debug: bugs are local — check the inputs, not 5 other systems.
# - Safe to parallelize: no shared state = no race conditions.
# - Portable: works anywhere because it depends only on its arguments.
# - Honest signature: inputs + return value tell you EVERYTHING it does.


# 22. Internal mutation doesn't break external purity
# ----------------------------------------------------
# - A function can mutate local variables and still be pure.
# - What matters is what the OUTSIDE WORLD can observe.
# - Example (pure despite mutating `total`):
#     def sumList(numbers):
#         total = 0
#         for n in numbers:
#             total += n        # internal mutation, invisible to caller
#         return total
# - This is why Uncle Bob's FromRoman.convert() is pure:
#   the object mutates itself internally, but is thrown away after each call.
#   From outside: convert("XIV") always returns 14, no side effects.


# 23. Push side effects to the edges
# -----------------------------------
# - Real software NEEDS side effects (I/O, state, etc.).
# - The useful pattern: keep the CORE LOGIC pure, do I/O at the boundary.
#   [edge: read input] → [PURE: compute] → [edge: print/save result]
# - In romanNumeralConverter.py:
#     convertRomanNumeralToInteger()  ← pure core (no print, no file)
#     if __name__ == "__main__":      ← impure edge (reads sys.argv, prints)


# 24. Objects as "scratchpads" for helper methods
# ------------------------------------------------
# - When many small helpers need to share state, passing it as arguments
#   everywhere gets ugly.
# - A class can hold that state as instance variables — helpers read/write
#   them instead of passing long parameter lists.
# - If the object is created fresh per call and thrown away, the outer
#   function stays pure even though the helpers mutate instance variables.
# - Tradeoff: small perf cost (allocation + GC) for readability.
#   Worth it unless you're writing embedded / real-time / game engine code.


# 25. Python import ordering (PEP 8 / isort)
# -------------------------------------------
# - Imports are grouped into 4 groups, separated by blank lines:
#     1. __future__         e.g. `from __future__ import annotations`
#     2. Standard library   e.g. `json`, `logging`, `os`
#     3. Third-party        e.g. `httpx`, `pytest`, `pandas`
#     4. First-party        your own project packages
# - Blank line between groups makes external vs internal deps visible at a glance.
# - Auto-enforced by tools like `ruff` / `isort` — you don't choose by hand.
# - Config lives in `pyproject.toml`:
#     [tool.ruff.lint.isort]
#     known-first-party = ["intellegam", "agents", "cli"]
# - Fix with: `ruff format` or `ruff check --fix`


# 26. "When is it enough?" — the three-lens test heuristic
# ---------------------------------------------------------
# - Coverage % is a metric; SCENARIOS are what actually matter.
# - For any function, walk through three lenses before shipping:
#
#     ┌──────────────────────────┬───────────────────────────────────────┐
#     │ Lens                     │ Question                              │
#     ├──────────────────────────┼───────────────────────────────────────┤
#     │ 1. Happy path            │ Does the main use case work E2E?      │
#     │ 2. Known failure modes   │ What specific failures should         │
#     │                          │ degrade gracefully?                   │
#     │ 3. Input/output boundary │ Are the edges of the contract         │
#     │                          │ respected? (malformed → "", not crash)│
#     └──────────────────────────┴───────────────────────────────────────┘
#
# - Example for a `scrape()` HTTP function:
#     1. Happy path        → expected body + return value
#     2. Failure modes     → 4xx/5xx, JSON decode errors, transport errors
#     3. Boundary          → malformed schemas return "" instead of crashing
# - Rule of thumb: if you can't answer all three, you haven't tested enough.
#   If you CAN answer all three, you're probably done — don't chase 100%.


# 27. Dependency Inversion Principle (DIP) — web_fetch case study
# ----------------------------------------------------------------
# Rule: "High-level policy should not depend on low-level details.
#        Both should depend on abstractions."
#
# Common misread: "they shouldn't depend on each other."
# Precise version: NEITHER knows the other exists; BOTH point UP at a
# shared contract.
#
# ── Today's web_fetch (violates DIP) ──────────────────────────────
#
#   web_fetch.py (policy)
#       │
#       │ imports
#       ▼
#   httpx.HTTPError, FirecrawlTargetSiteError, SecretProviderError, ...
#       (low-level concrete types from firecrawl, env, httpx)
#
# Symptom in the code:
#     except httpx.HTTPError as e:           → retry prompt
#     except FirecrawlTargetSiteError as e:  → target-error prompt
#     except SecretProviderError as e:       → ??? (kept flipping)
#
# The policy ("is this retriable?") needs SEMANTIC info, but reads it
# from low-level TYPES that don't carry that meaning. SecretProviderError
# alone can't tell you if it's a bad password (permanent) or a timeout
# (transient). That ambiguity caused the iteration loop with Codex.
# Swap Firecrawl → Brave, or Infisical → AWS Secrets, and every except
# clause has to be rewritten.
#
# ── Inverted version (follows DIP) ────────────────────────────────
#
#                  ┌────────────────────────────────┐
#                  │  abstract error contract:      │
#                  │   TransientFetchError          │
#                  │   PermanentFetchError          │
#                  │   TargetSiteError              │
#                  └─────────▲─────────────▲────────┘
#                            │             │
#                     depends│             │implements / raises
#                            │             │
#                     ┌──────┴──────┐ ┌────┴───────────┐
#                     │ web_fetch   │ │ firecrawl.py   │
#                     │ (policy)    │ │ env.py         │
#                     └─────────────┘ └────────────────┘
#
# Now web_fetch only catches the abstract types:
#     except TransientFetchError: → service-unavailable prompt
#     except PermanentFetchError: → config-invalid prompt
#     except TargetSiteError:     → target-error prompt
#
# The PROVIDER decides "is SecretProviderError(auth=bad) permanent or
# SecretProviderError(timeout) transient?" — because it has the context.
# web_fetch doesn't need to know.
#
# ── Why one-way coupling is already a violation ───────────────────
# - web_fetch imports firecrawl ✓
# - firecrawl does NOT import web_fetch ✗
# This is one-way coupling, not mutual. DIP is still violated because
# the arrow goes high → low. The fix is NOT making firecrawl import
# web_fetch (that's circular and worse) — it's introducing a third
# module both can point UP at.
#
# ── When to actually do the inversion ──────────────────────────────
# - With ONE provider (one scraper, one secret backend), the abstraction
#   tax can exceed the benefit. "Three similar lines > premature abstraction."
# - It pays off when:
#     • ≥2 providers (Firecrawl AND Brave both have env-classification issues)
#     • Low-level churn keeps forcing high-level rewrites
#     • The policy keeps misclassifying because the type can't carry the
#       semantic distinction (the SecretProviderError flip-flop)
# - Today: hard-coding is defensible. The iteration loop is the warning sign.


# 28. Records and Python's @dataclass — "data-only" carriers
# -----------------------------------------------------------
# UML diagrams in Clean Code use bubbles labeled:
#   C = Class       (data + behavior)
#   I = Interface   (contract only, no implementation)
#   R = Record      (data only, immutable, no behavior)
#
# A "record" is a labeled bag of values. No business logic, no mutation.
# Just fields you declared + auto-generated equals/hashCode/toString.
#
# ── Java ──
#   public record RentalItem(String type, int days, int unitPrice) { }
#
# ── Python equivalent: @dataclass ──
#   from dataclasses import dataclass
#
#   @dataclass(frozen=True)
#   class RentalItem:
#       type: str
#       days: int
#       unitPrice: int
#
# What @dataclass auto-generates for you:
#   - __init__         → RentalItem("PROJECTOR", 2, 50)
#   - __repr__         → print(item) shows all fields nicely
#   - __eq__           → value equality (two records with same fields are ==)
#   - __hash__         → usable as dict keys / in sets (when frozen)
#
# Useful flags:
#   @dataclass(frozen=True)   → immutable (assigning a field raises)
#   @dataclass(order=True)    → adds <, <=, >, >= comparing fields
#   @dataclass(slots=True)    → smaller memory, faster attribute access (3.10+)
#   @dataclass(kw_only=True)  → constructor requires keyword args (3.10+)
#
# Mutable defaults trap:
#   @dataclass
#   class Item:
#       tags: list[str] = []          # ❌ shared across ALL instances
#       tags: list[str] = field(default_factory=list)   # ✅ fresh list each time
#
# When to reach for what:
#   - @dataclass               → default answer for data carriers
#   - @dataclass(frozen=True)  → records / value objects (Java-record-like)
#   - typing.NamedTuple        → immutable, also indexable like a tuple
#   - pydantic.BaseModel       → when you need runtime validation / JSON
#   - plain dict               → when shape is dynamic or untyped
#
# When NOT to use @dataclass:
#   - The class has substantial behavior → that's a regular class
#   - You need extreme perf in hot loops → consider tuples or slots
#
# Mental model: a paper form with named fields. You fill in the blanks,
# pass it around, read it. You don't ask it to DO anything.


# 29. Test fundamentals — every line earns its place
# ---------------------------------------------------
# Tests are the executable specification of the system. Every choice
# answers ONE question: "when this fails three years from now, will the
# engineer reading it know what broke and what the system should do?"
#
# Anatomy of a well-formed test, line by line:
#
#   @Test                  / def test_*    → framework discovery hook
#   long behavioral name   → encodes scenario + EXPECTED OUTCOME
#   Arrange (setup state)  → minimum needed to trigger behavior
#   Act    (do the thing)  → ONE call, stored in a local for clarity
#   Assert (verify)        → length/structure first, then contents
#
# Naming rule: name = scenario + outcome.
#   - BAD:   testReceipt1
#   - OK:    oneLargeRoomAndCoffeeForWeekGetsCookies
#   - GOOD:  oneLargeRoomAndCoffeeForWeekGetsFreeCookieBonus
#   The word "free"/"bonus" makes the BUSINESS RULE explicit, not the
#   user-observable outcome alone.
#
# Why hard-code expected values (e.g. 675, 34) instead of recomputing:
#   if the test re-derives expected from the same logic as the code,
#   both can be wrong together and the test still passes. Literal
#   constants pin the human's intent.
#
# Why assert length BEFORE indexing into the array:
#   wrong length → IndexOutOfBounds on subsequent assertions = confusing
#   failure. Asserting length first produces "expected 3, got 2" =
#   clear failure.
#
# When to split a test:
#   Split when the two halves test INDEPENDENTLY MEANINGFUL behaviors.
#   Don't split when the value IS in the interaction between the parts.
#   The "one assertion per test" rule really means "one CONCEPT per
#   test" — multiple assertions verifying parts of the same fact is fine.


# 30. Test discovery: annotations vs naming conventions
# ------------------------------------------------------
# Frameworks need to know which methods are tests. Two strategies:
#
#   Java/JUnit:     @Test annotation on the method
#   Python/pytest:  function name starts with `test_`,
#                   file name starts with `test_` (or ends `_test.py`)
#
# Tradeoff:
#   - Annotations: explicit, compiler-checked, rename-safe.
#   - Conventions: zero boilerplate, but rename → test silently excluded.
# Both achieve the same goal — match the language's idiom.


# 31. Language naming conventions
# --------------------------------
# Match the language's convention; mixing styles looks jarring to readers.
#
#   ┌──────────────┬─────────────────┬──────────────────┐
#   │              │ Java / JS / C#  │ Python / Ruby    │
#   ├──────────────┼─────────────────┼──────────────────┤
#   │ Class        │ PascalCase      │ PascalCase       │
#   │ Method/Func  │ camelCase       │ snake_case       │
#   │ Variable     │ camelCase       │ snake_case       │
#   │ Constant     │ UPPER_SNAKE     │ UPPER_SNAKE      │
#   │ Package      │ lowercase.dot   │ lowercase_snake  │
#   └──────────────┴─────────────────┴──────────────────┘
#
# Not technically wrong to mix, but a Python reader sees camelCase func
# names as "this person came from Java." Idiomatic Python would write
# `convert_roman_numeral_to_integer` not `convertRomanNumeralToInteger`.


# 32. AAA / Given-When-Then — origin and meaning
# -----------------------------------------------
# Two unrelated "AAA"s:
#   - Video games "AAA": from bond credit ratings (AAA = top tier).
#     Pure marketing language for high-budget titles. Early '90s.
#   - Testing "AAA": Arrange / Act / Assert. Coined ~2001 by Bill Wake,
#     popularized by the TDD community.
#
# Same structure in BDD:
#       AAA               BDD
#       Arrange      ↔    Given (the world is in state X)
#       Act          ↔    When  (something happens)
#       Assert       ↔    Then  (we expect outcome Y)
#
# Why the label matters: once you have a name for the structure, you
# notice when tests are missing it. Tests without clear AAA tend to
# read chaotically; tests with it scan cleanly.


# 33. BDD basics — testing in plain language
# -------------------------------------------
# BDD = Behavior-Driven Development. Style of writing tests that focuses
# on describing behavior in natural language rather than implementation.
# Coined by Dan North (~2003-2006), evolved out of TDD.
#
# Same skeleton as AAA, different vocabulary:
#       Given  ↔  Arrange   (the world is in state X)
#       When   ↔  Act       (something happens)
#       Then   ↔  Assert    (we expect outcome Y)
#
# Two flavors:
#   - BDD-style code: just rename your AAA comments to Given/When/Then.
#     Still a plain unit test, just structured for readability.
#   - Full BDD with Gherkin/Cucumber: scenarios live in a separate
#     `.feature` file in natural language; framework maps each line
#     to a step function. Non-devs can read/write the .feature file.
#
# Example .feature:
#     Feature: Free cookie bonus
#       Scenario: Renting a large room with coffee for a week
#         Given a fresh order
#         When I rent a LARGE_ROOM for 5 days
#         And I rent COFFEE for 5 days
#         Then the receipt should have 3 items
#         And the receipt should contain free COOKIES
#
# Central claim: most bugs are misunderstanding, not coding errors.
# A shared natural-language spec catches misalignment between PM,
# designer, and engineer earlier than code review would.
#
# When it's worth the ceremony:
#   ✅ Non-technical stakeholders need to verify behavior
#   ✅ Complex acceptance criteria that should be living docs
#   ❌ Solo dev, internal libs, algorithmic code — overkill


# 34. BDD + agentic coding — research findings (as of 2026)
# ----------------------------------------------------------
# Pairing BDD with LLM agents is an active, promising research area.
# Key results published in 2025-2026:
#
# - BDDCoder (multi-agent framework, 4 roles: Programmer/Tester/
#   Requirements Analyst/User): feeding executable Gherkin scenarios
#   to the agent outperforms natural-language scenarios by up to 15.1%
#   on Pass@1 scores. Closed feedback loop ("does this test pass?")
#   beats open-ended prose requirements.
#
# - Industrial case (automotive): 95% of LLM-generated acceptance
#   scenarios rated "helpful" by engineers; 92% of generated scripts
#   were usable. Bottleneck = input quality, not generation quality.
#
# - Sloppy-input failure mode: without explicit rules, AI-generated
#   Gherkin drifts into vague Thens, UI-heavy scripts, multi-behavior
#   scenarios, placeholder examples. The fix is a Gherkin style guide
#   fed to the agent as context (see automationpanda's published
#   "gherkin-guidelines-for-ai").
#
# - Model-specific prompting matters:
#     Claude → chain-of-thought
#     GPT-4  → zero-shot
#     Gemini → few-shot
#
# - Emerging label "Spec-Driven Development (SDD)" = BDD applied
#   specifically to LLM-agent workflows.
#
# Why it fits agents structurally:
#   - Given/When/Then is literally the format LLMs are best at:
#     natural language + structure.
#   - Executable scenarios are the highest-bandwidth way to express
#     intent without writing the code yourself.
#   - It solves the "did I build the right thing?" failure mode —
#     the WORST failure mode with agents that generate fast and
#     plausibly-wrong.
#
# Lightweight personal adoption (no Cucumber, no .feature files):
#   When starting a feature with an agent, write the request as
#   Given/When/Then before asking for code. That alone captures
#   most of the benefit. The ceremony of full BDD tooling is
#   optional; the discipline of writing specs first is the lever.
