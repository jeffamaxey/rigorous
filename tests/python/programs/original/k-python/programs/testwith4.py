class A:
  def __enter__(self): pass
  def __exit__(self, type, value, traceback):
    return False

def a():
  with A():
    pass

a()
