import pytest
from romanNumeralConverter import convertRomanNumeralToInteger

def test_L_is_50(): assert convertRomanNumeralToInteger("L") == 50
def test_I_is_1(): assert convertRomanNumeralToInteger("I") == 1

def test_LV_is_55(): assert convertRomanNumeralToInteger("LV") == 55
def test_XVIII_is_18(): assert convertRomanNumeralToInteger("XVIII") == 18

def test_IX_is_9(): assert convertRomanNumeralToInteger("IX") == 9
def test_XC_is_90(): assert convertRomanNumeralToInteger("XC") == 90

# now testing wrong ones:
def test_IIII_is_rejected(): 
  with pytest.raises(ValueError): convertRomanNumeralToInteger("IIII")

def test_IC_is_rejected():
  with pytest.raises(ValueError): convertRomanNumeralToInteger("IC")
  