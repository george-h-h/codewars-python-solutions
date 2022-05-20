import vowel_count as vc

def test1():
  assert vc.get_count("hello") == 2

def test2():
  assert vc.get_count("bcd") == 0