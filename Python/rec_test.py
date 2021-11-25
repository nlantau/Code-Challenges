


def tak(x,y,z):
    if y < x:
        tak(tak(x-1,y,z),tak(y-1,z,x),tak(z-1,x,y))
    else:
        z
    

def tak2(x,y):
    if x < 1 or y < 1:
        return 0
    return 1 + tak2(x-1,y-2)

print(tak(5,4,5))