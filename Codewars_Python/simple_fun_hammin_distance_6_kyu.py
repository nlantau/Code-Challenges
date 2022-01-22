# nlantau, 2021-10-28

hamming_distance = lambda a,b: len([*filter(lambda x: x.strip('0'),f'{a^b:b}')])

print(hamming_distance(25,87))
