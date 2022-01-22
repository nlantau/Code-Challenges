# nlantau, 2020-11-08


def is_divisible(n, x, y):
    return (n % x == 0) & (n % y == 0)


print(is_divisible(3, 3, 4))
print(is_divisible(12, 3, 4))
print(is_divisible(8, 3, 4))
print(is_divisible(48, 3, 4))
