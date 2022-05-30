import two_to_one as tto

def test1():
  assert tto.longest("fedcba", "zyxwvu") == "abcdefuvwxyz"