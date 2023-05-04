for _ in range(3, 0, -1):
  y = 4
  while y > 0:
    y -= 1
    if y == 3: continue
    assert y != 3
    if y == 2:
      z = 2
  z = z + 1
assert z == 3
