# nlantau, 2021-02-01


a1 = [-1,5,10,20,28,3]
a2 = [26,134,135,15,17]

sample_output = [28,26]

def smallestDifference_passed7outof10(a, b):
    a.sort()
    b.sort()
    res = list()

    for i in a:
        t = max(a) + max(b)
        for j in b:
            if abs(j-i) < t:
                t = abs(j-i)
                res.clear()
                res.append(i)
                res.append(j)
    return res


def smallestDifference(a,b):
    a.sort()
    b.sort()
    idx_one = 0
    idx_two = 0
    smallest = float("inf")
    curr = float("inf")
    res = list()

    while idx_one < len(a) and idx_two < len(b):
        first = a[idx_one]
        second = b[idx_two]
        if first < second:
            curr = second - first
            idx_one += 1
        elif second < first:
            curr = first - second
            idx_two += 1
        else:
            return [first, second]
        if smallest > curr:
            smallest = curr
            res = [first, second]
    return res

print(smallestDifference(a1,a2))


