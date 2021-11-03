# nlantau, 2021-11-03

get_even_numbers=lambda x:[*filter(lambda y:~y&1, x)]

print(get_even_numbers([1,2,3,4,5]))
