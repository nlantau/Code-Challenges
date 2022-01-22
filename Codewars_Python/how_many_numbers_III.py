# nlantau, 2021-02-03

# Too slow. Passes test cases but fails on speed

# Time to beat: 2058 ms

import re


def find_all(sum_dig, digs):
    # digs set range ie digs = 3 -> from 100 to 999 (inclusive)
    # increasing order in first and second numb
    # sum_dig = what the sum of the digits in the number should equate
    # count each match
    # return [counter, first_match, last_match]

    d_reg = re.compile(r'\d')
    start = 1 * (10 ** (digs-1))   # 3 -> 1*10^2 = 100
    end = 1 * (10 ** digs)      # 3 -> 1*10^3 = 1000 (exclusive)

    print(start,end)
    counter = 0
    first_match = 0
    second_match = 0

    p = True
    for numb in range(start, end):
        # if numb is not in order, continue
        x = str(numb)
        for i in range(1, len(x)-1):
            if x[i] < x[i-1]:
                p = False
                break
        if not p:
            p = True
        else:

            dig_sum = 0
            #dig_list = d_reg.findall(str(numb))
            #dig_list = [int(i) for i in dig_list]
            dig_list = [int(i) for i in str(numb)]
            dig_list_sorted = sorted(dig_list)

            if dig_list_sorted != dig_list:
                continue

            dig_sum = sum(dig_list)

            if dig_sum == sum_dig:
                counter += 1
                if first_match == 0:
                    first_match = numb
                second_match = numb
    if counter == 0:
        return []
    return [counter, first_match, second_match]

print(find_all(10, 3))
print(find_all(27, 3))
print(find_all(84, 4))
print(find_all(35, 6))
