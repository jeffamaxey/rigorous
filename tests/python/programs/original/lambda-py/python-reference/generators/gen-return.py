def f():
    yield 1
    return

g = f()
assert next(g) == 1
try:
    next(g)
except StopIteration:
    pass
else:
    raise Exception("return inside of generator raises StopIteration")

try:
    next(g)
except StopIteration:
    pass
else:
    raise Exception("should have gotten StopIteration")
