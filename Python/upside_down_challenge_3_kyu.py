# nlantau, 2021-10-28

op_sing = {
        "1" : "1",
        "8" : "8",
        "0" : "0"
          }

op_mul = {
        "1" : "1",
        "6" : "9",
        "9" : "6",
        "8" : "8",
        "0" : "0"
        }

def upsidedown(x,y):
    r = y-x
    s = str(r)
    l = len(s)

    fh = s[:l//2]
    sh = s[l//2:]

    print("fh " + fh)
    print("sh " + sh)





upsidedown(0,25)
    
