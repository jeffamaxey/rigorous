# If this test fails, it is most likely due to an issue
# with the varargs implementation, rather than scoping
# per se. Of course, the function returner() should be
# closing over lst, and returning it, rather than any
# global definition thereof. 

def makeReturner(*lst):
  def returner():
    return lst
  return returner

def makeReturner2(**kwargs):
  def returner():
    return kwargs
  return returner

___assertEqual(makeReturner(1,2,3)(), (1,2,3))
___assertEqual(makeReturner2(a=11)()['a'], 11)
