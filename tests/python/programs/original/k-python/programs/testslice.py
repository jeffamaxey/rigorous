x = [0,1,2,25,4,50,6,100,8,9]

assert x[:] == x == x[:] == x[:20] == x[-20:] == x[:10:1]
assert x[3:9:2] == x[-7:-1:2] == [25,50,100]
assert x[5:4] == x[4:5:-1] == x[:0] == []
assert x[7:2:-2] == x[-3:-8:-2] == [100,50,25]
assert x[::-1] == [9, 8, 100, 6, 50, 4, 25, 2, 1, 0]
