for x in range(2, -1, -1):
  y = 3
  while y > 0:
    y -= 1
    if y == 2: break
    assert y >= 2
  z = x
assert z == 0
