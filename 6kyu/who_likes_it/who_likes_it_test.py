import who_likes_it as wli

def test1():
  assert wli.likes(["Shin", "Rem", "Lelouch", "Eren"]) == "Shin, Rem and 2 others like this"

def test2():
  assert wli.likes([]) == "no one likes this"

def test3():
  assert wli.likes(["Alphonse"]) == "Alphonse likes this"