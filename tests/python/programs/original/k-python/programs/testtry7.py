try:
  try:
    raise
  except a:
    assert False
except NameError:
  x = 9
assert x == 9
