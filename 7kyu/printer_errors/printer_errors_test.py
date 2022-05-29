import printer_errors as pe

def test1():
  assert pe.printer_error("abcxyz") == "3/6"

def test2():
  assert pe.printer_error("123456789d") == "9/10"