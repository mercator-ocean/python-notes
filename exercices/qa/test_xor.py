import pytest
from .log_qa import xor


def test_xor():
    assert xor(True, False) == True
    assert xor(False, True) == True
    assert xor(False, False) == False
    assert xor(True, True) == False


def test_raises_when_not_boolean():
    with pytest.raises(TypeError):
        xor("titi", False)
