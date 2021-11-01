# nlantau, 2021-10-11

"""
test.assert_equals(iq_test("2 4 7 8 10"),3)
test.assert_equals(iq_test("1 2 2"), 1)
"""

a="2 4 7 8 10"
b="1 2 1 1"
c="1 2 2"

def iq_test(a):
    b=[*filter(lambda x:~x&1,map(int,a.split()))]
    c=[*filter(lambda x:x&1,map(int,a.split()))]
    return a.split().index(str(*[b,c][len(c)<len(b)])) +1

#x=[b,c][len(c)<len(b)]


print(a,iq_test(a))
print(b,iq_test(b))
print(c,iq_test(c))
