x = 3
y = 1
while x > 0:
  x -= 1
  try:
    continue
  finally:
    y = y + 1
  assert False
assert y == 4
