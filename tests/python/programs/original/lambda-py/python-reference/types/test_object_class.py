def test_object_class():
    # Testing object class...
    a = object()
    ___assertEqual(a.__class__, object)
    ___assertEqual(type(a), object)
    b = object()
    #___assertNotEqual(a, b) Not defined in python-lib-bindings (Alejandro)
    ___assertTrue(a != b)
    ___assertFalse(hasattr(a, "foo"))

    try:
        a.foo = 12
    except (AttributeError, TypeError):
        pass
    else:
        assert False, "object() should not allow setting a foo attribute"
    ___assertFalse(hasattr(object(), "__dict__"))

    class Cdict(object):
        pass
    x = Cdict()
    ___assertEqual(x.__dict__, {})
    x.foo = 1
    ___assertEqual(x.foo, 1)
    x.__dict__['bar'] = 2
    ___assertEqual(x.bar, 2)
    del x.__dict__['bar']
    ___assertEqual(x.__dict__, {'foo': 1})

    class F:
        def __init__(self, name):
            self.name = name

    m = F("a")
    m.__dict__ = {'x':3}
    ___assertFalse(hasattr(m, "name"))
    ___assertEqual(m.x, 3)
    del m.__dict__
    ___assertEqual(m.__dict__, {})

test_object_class()
