# see https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python

def factorial(n):
  factorial = 1
  if n == 0:
    return factorial
  elif n > 0:
    for x in range(1, n+1):
      factorial = factorial * x
    return factorial
  else:
    raise ValueError("Let's not start the debate about negative factorials of real numbers.")