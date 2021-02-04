# nlantau, 2021-02-04

# passed

s = "abcd\nefgh\nijkl\nmnop"

def vert_mirror(s):
    ss = s.split()
    t = list()
    for x in ss:
        t.append(x[::-1])
        t.append('\n')
    return "".join([i for i in t[:len(t)-1]])
        


def hor_mirror(s):
    ss = s.split()
    t = list()
    for i in range(len(ss)-1, -1, -1):
        t.append(ss[i])
        t.append('\n')
    return "".join([i for i in t[:len(t)-1]])


def opert(fct, s):
    return fct(s)


print(s)
#print(opert(vert_mirror, s))
print(opert(hor_mirror, s))
