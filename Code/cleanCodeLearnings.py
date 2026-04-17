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
