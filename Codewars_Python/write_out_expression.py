operators = {
    "+": "Plus",
    "-": "Minus",
    "*": "Times",
    "/": "Divided By",
    "**": "To The Power Of",
    "=": "Equals",
    "!=": "Does Not Equal",
}


numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
}

import re


def expression_out(equation: str):
    num_one = re.findall(r"[0-9]{1,2}", equation)
    one = num_one[0]
    two = num_one[1]
    op = re.findall(r"[-+*!=/]{1,2}", equation)
    op2 = "".join(op)
    result = ""
    result2 = ""
    result3 = ""
    print(op)
    if len(op) < 1:
        return "That's not an operator!"
    print(num_one)
    if one in numbers.keys():
        result = numbers[one]

    if two in numbers.keys():
        result2 = numbers[two]

    if op2 in operators.keys():
        result3 = operators[op2]

    return result + " " + result3 + " " + result2


print(expression_out("10 * 10"))
