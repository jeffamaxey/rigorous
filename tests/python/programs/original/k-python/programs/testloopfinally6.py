for x in (2, 3, 4):
  try:
    break
  finally:
    y = 6
    assert x == 2
  assert False
assert y == 6
