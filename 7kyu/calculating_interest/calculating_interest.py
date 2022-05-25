# see https://www.codewars.com/kata/59cd0535328801336e000649/train/python

def interest(p, r, n):
  simple_interest = p * ((r * n) + 1)
  compound_interest = p * ((r + 1) ** n)
  return [round(simple_interest), round(compound_interest)]