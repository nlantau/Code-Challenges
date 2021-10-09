#!/usr/bin/python
"""
test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
test.assert_equals(order(""), "")
"""
a = "is2 Thi1s T4est 3a"
a = "4of Fo1r pe6ople g3ood th5e the2"

order = lambda a:" ".join((lambda v:[v[e]for e,k in enumerate(v.keys())])({int(k)-1:a.split()[e]for e,k in enumerate([*filter(str.isdigit,a)])}))

print(a)
print(f'{order(a)}')

# Clever solutions
"""
order = lambda xs: ' '.join(sorted(xs.split(), key=min))

def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))


"""
