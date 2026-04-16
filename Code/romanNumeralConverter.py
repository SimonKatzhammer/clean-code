# code -> tests
# package FromRoman -> like a python folder / module

"""

  Java:
  fromRoman/
  └── FromRoman.java
  // FromRoman.java
  package fromRoman;          ← namespace declaration (folder)

  public class FromRoman {    ← the class
      public static int convert(String r) { ... }
  }

  Python equivalent:
  fromRoman/
  ├── __init__.py
  └── from_roman.py
  # from_roman.py
  class FromRoman:            ← the class
      @staticmethod
      def convert(r): ...
"""
"""
cd /Users/kaizen/Repositories/clean-code/Code
  source ../.venv/bin/activate
  python -c "from romanNumeralConverter import convertRomanNumeralToInteger; print(convertRomanNumeralToInteger('III'))"

"""

# values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}

def convertRomanNumeralToInteger(romanNumeral: str) -> int:
  totalSum = 0
  values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
  for i in range(len(romanNumeral)):
    if i+1 < len(romanNumeral):
      if values[romanNumeral[i]] < values[romanNumeral[i+1]]: 
        totalSum -= values[romanNumeral[i]]
      else:
        totalSum += values[romanNumeral[i]]
    else:
      totalSum += values[romanNumeral[i]]
  return totalSum

"""
def checkForNextCharSubstractIfSmaller(romanChar: str, i: int):
  if values[romanChar[i+1]] < values[romanChar[i]]: 
    integerValue = values[romanChar[i+1]] - values[romanChar[i]]
  else: 
    integerValue += values[romanChar[i]]
  return integerValue
"""  
  
  