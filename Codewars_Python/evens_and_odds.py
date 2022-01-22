# nlantau, 2020-11-09


def evens_and_odds(n):
    return f"{n:b}" if n % 2 == 0 else f"{n:x}"


print(evens_and_odds(1))
print(evens_and_odds(2))
print(evens_and_odds(3))
print(evens_and_odds(13))
