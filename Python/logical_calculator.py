# nlantau, 2020-11-07
"""
Test.describe('Basic tests')
Test.assert_equals(logical_calc([True, False], "AND"), False)
Test.assert_equals(logical_calc([True, False], "OR"), True)
Test.assert_equals(logical_calc([True, False], "XOR"), True)

Test.assert_equals(logical_calc([True, True, False], "AND"), False)
Test.assert_equals(logical_calc([True, True, False], "OR"), True)
Test.assert_equals(logical_calc([True, True, False], "XOR"), False)
"""


def logical_calc(array, op) -> bool:
    if op == "AND" and len(array) > 1:
        return (
            array[0] & array[1]
            if len(array) == 2
            else logical_calc((([array[0] & array[1]]) + array[2:]), "AND")
        )
    elif op == "OR" and len(array) > 1:
        return (
            array[0] | array[1]
            if len(array) == 2
            else logical_calc((([array[0] | array[1]]) + array[2:]), "OR")
        )
    elif op == "XOR" and len(array) > 1:
        return (
            array[0] ^ array[1]
            if len(array) == 2
            else logical_calc((([array[0] ^ array[1]]) + array[2:]), "XOR")
        )
    else:
        return array[0]


print(logical_calc([True, False], "AND"))
print(logical_calc([True, True, False], "OR"))
print(logical_calc([True, True, False], "AND"))
print(logical_calc([True], "AND"))
