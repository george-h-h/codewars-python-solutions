import calculating_with_functions as cwf

def test1():
  assert cwf.eight(cwf.plus(cwf.six())) == 14

def test2():
  assert cwf.seven(cwf.minus(cwf.two())) == 5

def test3():
  assert cwf.six(cwf.times(cwf.three())) == 18

def test4():
  assert cwf.nine(cwf.divided_by(cwf.three())) == 3

def test5():
  assert cwf.five(cwf.divided_by(cwf.two())) == 2