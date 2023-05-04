d = {1: 100, 2: 20} | {1:1, 2:2, 3:3}
___assertEqual(d, {1:1, 2:2, 3:3})

d.update()
___assertEqual(d, {1:1, 2:2, 3:3})

___assertRaises((TypeError, AttributeError), d.update, None)
