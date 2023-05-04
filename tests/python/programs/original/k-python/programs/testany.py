assert not any(())
assert any((1,)), any((1,))
assert not any((0,))
assert not any((0, 0, 0, 0))
assert any((0, 0, 0, 1))

class A:
  x = 0
  def __bool__(self): A.x += 1; return True

assert any((A(), A(), A(), A()))
assert A.x == 1
