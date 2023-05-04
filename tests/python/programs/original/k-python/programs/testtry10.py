try:
  try:
    raise
  finally:
    x = 11
  assert False
except RuntimeError:
  y = 12
  assert x == 11
assert y == 12
