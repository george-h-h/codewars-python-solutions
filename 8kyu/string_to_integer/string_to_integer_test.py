import string_to_integer as sti

def test1():
  assert sti.string_to_number("86") == 86

def test2():
  assert sti.string_to_number("-2000") == -2000