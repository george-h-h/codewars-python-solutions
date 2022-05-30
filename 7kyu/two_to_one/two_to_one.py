# see https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

def longest(a1, a2):
  new_string = ""
  for x in a1 + a2:
    if x not in new_string:
      new_string += x
  return "".join(sorted(new_string))