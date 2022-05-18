import return_negative as rn

def test1():
  assert rn.make_negative(4) == -4

def test2():
  assert rn.make_negative(0) == 0

def test3():
  assert rn.make_negative(-3) == -3