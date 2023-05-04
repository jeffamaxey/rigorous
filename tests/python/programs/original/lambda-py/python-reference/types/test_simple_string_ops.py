if 'xyz' + 'abcde' != 'xyzabcde': raise Exception('string concatenation')
if 'xyz'*3 != 'xyzxyzxyz': raise Exception('string repetition *3')
if 0*'abcde' != '': raise Exception('string repetition 0*')
if min('abc') != 'a' or max('abc') != 'c': raise Exception('min/max string')
if 'a' not in 'abc' or 'b' not in 'abc' or 'c' not in 'abc' or 'd' in 'abc':
    raise Exception('in/not in string')
