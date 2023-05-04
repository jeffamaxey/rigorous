class A:
    def sm2(self):
        return f"Hello {self}"
    sm2 = staticmethod(sm2)

___assertEqual(A.sm2("World"), "Hello World")
___assertEqual(A().sm2("World"), "Hello World")
