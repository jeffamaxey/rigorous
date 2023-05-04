l0_3 = [0, 1, 2, 3]
l0_3_bis = list(l0_3)
if l0_3 != l0_3_bis: raise Exception('List identity 1')
if l0_3 is l0_3_bis: raise Exception('List identity 2')
if list(''): raise Exception( 'List string 1')
if list('spam') != ['s', 'p', 'a', 'm']: raise Exception( 'List string 2')
