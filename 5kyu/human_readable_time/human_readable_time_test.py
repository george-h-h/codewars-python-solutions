import human_readable_time as hrt

def test1():
  assert hrt.make_readable(254) == "00:04:14"

def test2():
  assert hrt.make_readable(357586) == "99:19:46"