# see https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(sentence):
  count = 0
  vowels = ["a", "e", "i", "o", "u"]
  for x in sentence:
    if x in vowels:
      count += 1
  return count