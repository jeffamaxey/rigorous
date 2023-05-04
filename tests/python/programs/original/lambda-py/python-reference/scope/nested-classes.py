
try: 
 class C(object):
  x = 4
  class D(object):
   y = x
except:
 pass
else:
 assert False 

