def b():
  global x
  try:
    x = 9
    return 5
  finally:
    assert x == 9
    x = 10
  assert False

assert b() == 5
assert x == 10
