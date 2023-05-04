def grange(n):
	yield from range(n)

def outergen(n):
	yield from grange(n)

___assertEqual(list(outergen(10)), list(range(10)))