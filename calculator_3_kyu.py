#!/usr/bin/python
# nlantau, 2021-11-01

"""
Create a simple calculator that given a string of operators (), +, -, *, / and
numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7

Remember about the order of operations! Multiplications and divisions have a
higher priority and should be performed left-to-right.
Additions and subtractions have a lower priority and should also be performed left-to-right.
"""


class Calculator:
    def __init__(self):
        self.op = {
                '+' : lambda a,b:a+b,
                '-' : lambda a,b:a-b,
                '*' : lambda a,b:a*b,
                '/' : lambda a,b:a/b,
                }

    def evaluate(self, string):
        return self.to_tree(string)

    def to_tree(self, expression):
        tree = dict()
        msg =""
        stack = list()
        for char in expression:
            if(char == '('):
                stack.append(msg)
                msg = ""
            elif char == ')':
                parent = stack.pop()
                if parent not in tree:
                    tree[parent] = list()
                tree[parent].append(msg)
                msg = parent
            else:
                msg += char
        return tree

print(Calculator().evaluate("2 / 2 + 3 * 4 - 6")) # => 7

print(Calculator().op['+'](1,2))

"""
Plan:
    PEMDAS = Parentheses, exponents, multiplication & division, addition & subtraction


"""
