class A:
    # this
    @classmethod
    def cm1(cls):
        return cls
    # is just syntactic sugar for:
    def cm2(self):
        return self
    cm2 = classmethod(cm2)

___assertEqual(A.cm1(), A)
___assertEqual(A().cm1(), A)
___assertEqual(A.cm2(), A)
___assertEqual(A().cm2(), A)
