import counting_sheep as cs

def test1():
  assert cs.count_sheeps([True, False, True]) == 2

def test2():
  assert cs.count_sheeps([True, False, True, False, False, "wakuwaku", True, False, True, True]) == 5