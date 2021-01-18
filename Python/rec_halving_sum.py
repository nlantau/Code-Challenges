# nlantau, 2021-01-18

def halving_sum(n):
    if n <= 0:
        return 0
    return n + halving_sum(n//2)

print(halving_sum(25))
