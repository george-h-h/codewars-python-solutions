import sum_of_positive as sop

def test1():
  assert sop.positive_sum([3, 5]) == 8

def test2():
  assert sop.positive_sum([0, -11]) == 0

def test3():
  assert sop.positive_sum([-3, -4, 7, 0, 2]) == 9