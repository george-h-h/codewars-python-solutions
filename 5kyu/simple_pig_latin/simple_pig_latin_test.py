import simple_pig_latin as spl

def test1():
  assert spl.pig_it("Hello George") == "elloHay eorgeGay"

def test2():
  assert spl.pig_it("Lena is looking at Shin") == "enaLay siay ookinglay taay hinSay"