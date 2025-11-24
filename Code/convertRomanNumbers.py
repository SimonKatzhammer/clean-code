# I -> III -> IV -> V -> VI -> IX -> X -> XI -> XIV -> XV -> XVI -> XIX -> XX -> XXI -> XXIV -> XXXIX -> XL

#parts: 
    # input a number -> convert to roman numeral -> output roman numeral
    # Input: (positive) integer
    # Output: string (roman numeral)
    #E.g. 3331 -> "MMMCCCXXXI"

# lets go with tests!
# FRAMEWORK:
##


value_map = [
      (1000, 'M'),
      (900, 'CM'),  
      (500, 'D'),
      (400, 'CD'),
      (100, 'C'),
      (90, 'XC'),
      (50, 'L'),
      (40, 'XL'),
      (10, 'X'),
      (9, 'IX'),
      (5, 'V'),
      (4, 'IV'),
      (1, 'I'),
]

def convertIntToRomanNumber(num: int)-> str:
    RomanNumber = ""
    for value, symbol in value_map:
        multiple_symbol = num // value
        if multiple_symbol:
            RomanNumber += symbol * multiple_symbol
            num -= (value * multiple_symbol)
    return RomanNumber





def main():
    output = convertIntToRomanNumber(999)
    print(output)

main()





#reverse:
# 1 is I
# 2 is II
# 3 is III
# 4 is IV
# 5 is V
# 6 is VI
# 7 is VII
# 8 is VIII
# 9 is IX
# 10 is X
# 11 is XI
# 14 is XIV
# 15 is XV
# 16 is XVI
# 19 is XIX
# 20 is XX
# 21 is XXI
# 24 is XXIV
# 39 is XXXIX
# 40 is XL
# 50 is L
# 100 is C
# 500 is D
# 1000 is M

# for each number in int_num:
#    convert(number) -> roman_numeral



# I is 1
# V is 5
# X is 10
# L is 50
# C is 100
# D is 500
# M is 1000

# 33 -> XXXIII == X + X + X + I + I + I == 10 + 10 + 10 + 1 + 1 + 1

"""
def convertIntToRomanNumber(num: int)-> str:
    if num <= 0:
        return "Input must be a positive integer"
    if num == 1:
        return "I"
    if num == 2:
        return "II"
    if num == 3:
        return "III"
    if num == 4:   
        return "IV"
    if num == 5:   
        return "V"
    if num == 6:
        return "VI"
    if num == 7:
        return "VII"
    if num == 8:
        return "VIII"
    if num == 9:
        return "IX"
    else:
        return "Number out of range"


def int_to_roman(num)-> str:
    return convertRomanNumbers(num)

def convertRomanNumbers(num: int)-> str:
    if num <= 0:
        return "Input must be a positive integer"
    if num == 1:
        return "I"
    if num == 2:
        return "II"
    if num == 3:
        return "III"
    if num == 4:   
        return "IV"
    if num == 5:   
        return "V"
    if num == 6:
        return "VI"
    if num == 7:
        return "VII"
    if num == 8:
        return "VIII"
    if num == 9:
        return "IX"
    if num == 10:
        return "X"
    if num == 11:
        return "XI"
    if num == 19:
        return "XIX"
    if num == 20:
        return "XX"
    if num == 24:
        return "XXIV"
    if num == 40:
        return "XL"
    if num == 50:
        return "L"

"""




