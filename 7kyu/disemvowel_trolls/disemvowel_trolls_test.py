import disemvowel_trolls as dt

def test1():
  assert dt.disemvowel("Hello George") == "Hll Grg"

def test2():
  assert dt.disemvowel("It's been a long time, Handler One.") == "t's bn  lng tm, Hndlr n."