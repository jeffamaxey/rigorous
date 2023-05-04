assert all(())
assert all((1,))
assert not all((0,))
assert all((1,2,3,4))
assert not all((1,2,3,4,0))

class A:
  x = 0
  def __bool__(self): A.x += 1; return False

assert not all((A(), A(), A(), A()))
assert A.x == 1
