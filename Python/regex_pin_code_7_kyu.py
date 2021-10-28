# nlantau, 2021-10-28

validate_pin = lambda p:len([*filter(str.isdigit,p)]) == len(p) and
(len(p)==6 or len(p)==4)

print(validate_pin("1a34"))
