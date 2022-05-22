# see https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(string):
  vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  for x in string:
    if x in vowels:
      string = string.replace(x, "")
  return string