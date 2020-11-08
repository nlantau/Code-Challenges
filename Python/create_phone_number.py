# nlantau, 2020-11-07
"""
Write a function that accepts an array of 10 integers
(between 0 and 9), that returns a string of those
numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) #
=> returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!

Test.describe("Basic tests")
Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
Test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
Test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
Test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
Test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")
"""


def create_phone_number(n):
    return (
        "(abc) def-ghij".replace("a", str(n[0]))
        .replace("b", str(n[1]))
        .replace("c", str(n[2]))
        .replace("d", str(n[3]))
        .replace("e", str(n[4]))
        .replace("f", str(n[5]))
        .replace("g", str(n[6]))
        .replace("h", str(n[7]))
        .replace("i", str(n[8]))
        .replace("j", str(n[9]))
    )


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
