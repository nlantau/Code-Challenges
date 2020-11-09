# nlantau, 2020-11-09
"""
Is the number even?
If the numbers is even return true. If it's odd, return false.


Oh yeah... the following symbols/commands have been disabled!

use of ```%```
use of ```.even?``` in Ruby
use of ```mod``` in Python
"""


def is_even(n):
    # return "false" if (n & 1) else "true"
    return bool(~n & 1)


print(is_even(3))
print(is_even(14))
print(is_even(15))
print(is_even(26))
print(is_even(27))