def a():
  yield 5
  raise TypeError

b=a()

assert b.__next__() == 5
try: 
  b.__next__()
  assert False
except TypeError:
  try:
    b.__next__()
    assert False
  except StopIteration:
    x = 5

assert x == 5
