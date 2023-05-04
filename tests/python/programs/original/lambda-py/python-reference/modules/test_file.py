source = "a.txt"
with open(source, "w") as f:
    f.write("hello\n")
    f.write("world\n")
with open(source, "r") as f:
    ___assertEqual(f.read(), "hello\nworld\n")
    ___assertEqual(f.read(), "")
with open(source, "r") as f:
    ___assertEqual(f.readline(), "hello\n")
    ___assertEqual(f.readline(), "world\n")
