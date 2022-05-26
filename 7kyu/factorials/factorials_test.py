import pytest
import factorials as factorials

def test1():
  assert factorials.factorial(5) == 120

def test2():
  assert factorials.factorial(0) == 1

def test3():
  with pytest.raises(ValueError):
    factorials.factorial(-86)