# see https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
  result = 0
  for x in range(number):
    if x % 3 == 0 or x % 5 == 0:
      result += x
  return result