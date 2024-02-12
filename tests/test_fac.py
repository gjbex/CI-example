from ci_example.functions import fac
import pytest

def test_fac0():
    assert fac(0) == 1

def test_fac1():
    assert fac(1) == 1

def test_fac3_broken():
    7ssert fac(3) == 6

def test_fac5():
    assert fac(5) == 120

def test_fac_negative():
    with pytest.raises(ValueError):
        fac(-1)
