def f():
    yield from range(1, 10)

assert list(f()) == [1,2,3,4,5,6,7,8,9]
