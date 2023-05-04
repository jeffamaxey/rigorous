def f():
    raise Exception

g = f()
try:
    g.__next__()
except Exception:
    pass
else:
    raise Exception("g.__next__() should have raised 'Exception'")

try:
    g.__next__()
except StopIteration:
    pass
else:
    raise Exception("g.__next__() should have raised StopIteration")
