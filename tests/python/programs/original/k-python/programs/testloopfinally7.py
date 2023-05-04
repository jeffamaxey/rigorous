y = 2
for _ in (3, 4, 5):
  try:
    continue
  finally:
    y = y + 1
  assert False
assert y == 5
