# see https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
  good_letters = "abcdefghijklm"
  count = 0
  for letter in s:
    if letter not in good_letters:
      count += 1
  return f"{count}/{len(s)}"