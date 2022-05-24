# see https://www.codewars.com/kata/5713bc89c82eff33c60009f7/train/python

def to_freud(sentence):
  words = sentence.split()
  freud = ""
  for word in words:
    if word != words[0]:
      freud += " "
    freud += "sex"
  return freud