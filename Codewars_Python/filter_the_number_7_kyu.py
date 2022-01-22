# nlantau, 2021-11-03

filter_string=lambda a:int("".join(filter(str.isdigit, a)))

print(filter_string("123"))
