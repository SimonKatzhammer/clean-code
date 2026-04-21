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
