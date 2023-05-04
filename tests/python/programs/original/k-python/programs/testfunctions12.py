def a(* x, **y):
  assert not x
  assert not y

assert a() is None
