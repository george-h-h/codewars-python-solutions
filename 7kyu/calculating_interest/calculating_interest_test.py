import calculating_interest as ci

def test1():
  assert ci.interest(100, 0.1, 5) == [150, 161]

def test2():
  assert ci.interest(500, 0.3, 8) == [1700, 4079]