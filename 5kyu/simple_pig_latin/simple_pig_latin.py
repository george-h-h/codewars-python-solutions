# see https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(text):
  words = text.split()
  pig = ""
  for word in words:
    if word != words[0]:
      pig += " "
    if word.isalpha() == True:
      pig += word[1:] + word[0] + "ay"
    else:
      pig += word
  return pig