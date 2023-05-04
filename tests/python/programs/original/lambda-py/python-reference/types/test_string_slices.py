a = '0123456789'
if a[::] != a: raise Exception('Slice total')
if a[::2] != '02468': raise Exception('Slice 2')
if a[1::2] != '13579': raise Exception('Slice 1::2')

if a[::-2] != '97531': raise Exception('Slice ::-2')
if a[3::-2] != '31': raise Exception('Slice 3::-2')
if a[-100:100:] != a: raise Exception('Slice -100::100')
if a[100:-100:-1] != a[::-1]: raise Exception('Slice triple')
if a[-100:100:2] != '02468': raise Exception('Slice triple 2')
