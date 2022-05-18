# see https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python

def positive_sum(arr):
  total = 0
  for x in arr:
    if x > 0:
      total += x
  return total