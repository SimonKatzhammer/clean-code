# source .venv/bin/activate
# for pytest to run
# run by typing `pytest` in terminal

import pytest
from convertRomanNumbers import convertIntToRomanNumber

def test_non_integer_input_raises_type_error():
    with pytest.raises(TypeError):
        convertIntToRomanNumber("10")

    with pytest.raises(TypeError):
        convertIntToRomanNumber(3.14)

    with pytest.raises(TypeError):
        convertIntToRomanNumber(None)
