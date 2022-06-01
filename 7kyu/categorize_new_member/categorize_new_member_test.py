import categorize_new_member as cnm

def test1():
  assert cnm.open_or_senior([[56, 9], [58, 6], [36, 22]]) == ["Senior", "Open", "Open"]