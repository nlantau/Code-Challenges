from collections.abc import Iterable
"""
def flatten(i):
    for x in i:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x

def sum_nested(l):
    return sum(list(flatten(l)))
"""
def sum_nested(l):
    if len(l) <= 0:
        return 0
    else:
        if isinstance(l[0], list):
            return sum_nested(l[0]) + sum_nested(l[1:])
        else:
            return l[0] + sum_nested(l[1:])


print(sum_nested([1,2,3,4]), "== 10")
print(sum_nested(list(range(11))), "== 55")
print('Non-nested edge case')
print(sum_nested([]), "==0")
print('Should handle simple nestings')
print(sum_nested([[1], []]), "==1")
print(sum_nested([[1, 2, 3, 4]]), "==10")
print('Simple nesting edge case')
print(sum_nested([[], []]), "==0")

print('Should handle more complex nestings')
print(sum_nested([1, [1], [[1]], [[[1]]]]), "==4")
print(sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]]), "==8")
print('Complex nesting edge case')
