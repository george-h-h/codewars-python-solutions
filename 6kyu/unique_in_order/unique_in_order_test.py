import unique_in_order as uio

def test1():
  assert uio.unique_in_order("abccd") == ["a", "b", "c", "d"]

def test2():
  assert uio.unique_in_order([8, 8, 8, 6, 6]) == [8, 6]