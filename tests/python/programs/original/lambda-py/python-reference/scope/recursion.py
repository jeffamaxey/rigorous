def f(x):
    def fact(n):
        return 1 if n == 0 else n * fact(n - 1)

    if x >= 0:
        return fact(x)
    else:
        raise ValueError("x must be >= 0")

___assertEqual(f(6), 720)
