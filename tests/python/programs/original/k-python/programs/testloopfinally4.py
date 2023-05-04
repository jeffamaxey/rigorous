x = 8
while x > 0:
  try:
    x -= 1
  finally:
    break
  assert False
else:
  assert False
assert x == 7
