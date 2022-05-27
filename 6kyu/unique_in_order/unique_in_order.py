# see https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(iterable):
  result = []
  for x in list(iterable):
    if not result or x != result[-1]:
      result.append(x)
  return result