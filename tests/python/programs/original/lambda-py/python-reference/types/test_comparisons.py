if not 0 < 1 <= 1 == 1 >= 1 > 0 != 1:
    raise Exception('int comparisons failed')
if not 0.0 < 1.0 <= 1.0 == 1.0 >= 1.0 > 0.0 != 1.0:
    raise Exception('float comparisons failed')
if not '' < 'a' <= 'a' == 'a' < 'abc' < 'abd' < 'b':
    raise Exception('string comparisons failed')
if None is not None:
    raise Exception('identity test failed')
