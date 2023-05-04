def f():
    yield (yield 1)

g = f()
assert next(g) == 1
assert g.send(2) == 2
