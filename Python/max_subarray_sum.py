# nlantau, 2021-01-17

def max_sequence(a):
    msf=0
    meh=0
    s=len(a)
    for i in range(0,s):
        meh+=a[i]
        if(msf<meh):
            msf=meh
        if meh<0:
            meh=0
    return msf

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

