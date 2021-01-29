# nlantau, 2021-01-29

# Calculate the ratios of its elements that are positive,
# negative, and zero

arr = [1,1,0,-1,-1]

def plusMinus(arr):
    a = len(arr)
    pc = 0
    nc = 0
    zc = 0
    for i in arr:
        if i > 0:
            pc +=1
        elif i == 0:
            zc += 1
        else:
            nc += 1

    pcr = pc/a
    ncr = nc/a
    zcr = zc/a
    print(f"{pcr:.6f}")
    print(f"{ncr:.6f}")
    print(f"{zcr:.6f}")


plusMinus(arr)
