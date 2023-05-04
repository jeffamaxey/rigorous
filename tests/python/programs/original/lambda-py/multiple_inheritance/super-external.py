class A:
    def f(self):
        return 'A'
 
# super() in an external function
def external():
    f'{super().f()}E'

class EE(A):
    def f(self):
        return external()

# SystemError("super(): no arguments")
___assertRaises(SystemError, EE().f)
