def greet():
    return f'{"".join(["".join(chr(i)) for i in [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33]])}'


print(greet())
