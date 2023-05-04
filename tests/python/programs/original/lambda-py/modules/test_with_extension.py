# test reading the module correctly
# this test can be used to test .pyc

import sys
import support

def test_with_extension(ext):
    source = support.TESTFN + ext
    # write the statement to the source file
    # for testing the module.
    try:
        f = open(source, "w")
        f.write(f"# This tests Python's ability to import a {ext}file.")
        a = 10
        b = 15
        f.write(f"a ={a}")
        f.write(f"b ={b}")
    except:
        ___fail("open error")

    try:
        mod = __import__(support.TESTFN)
    except ImportError as err:
        ___fail("import error")
    # checking the module
    ___assertEqual(mod.a, a)
    # checking the module
    ___assertEqual(mod.b, b)

test_with_extension(".py")
