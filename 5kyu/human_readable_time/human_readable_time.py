# see https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(seconds):
  hours = str(int(seconds / 3600))
  minutes = str(int((seconds % 3600) / 60))
  seconds = str(int((seconds % 3600) % 60))
  return f"{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}"