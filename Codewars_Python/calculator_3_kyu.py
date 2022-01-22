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


class Calculator2:
    def __init__(self):
        self.op = {
                '+' : lambda a,b: float(a)+float(b),
                '-' : lambda a,b: float(a)-float(b),
                '*' : lambda a,b: float(a)*float(b),
                '/' : lambda a,b: float(a)/float(b),
                }

    def evaluate(self, s):
        s = s.split()
        print("expression:", s)
        if '(' in s and ')' in s:
            lp,rp = self.find_inner_paren(s)
            exp = s[lp+1:rp]
            print("exp: ",exp)
            s = s[:lp] + [self.op[exp[1]](exp[0],exp[2])] + s[rp+1:]
            return self.evaluate(" ".join([str(c) for c in s]))
        s = self.op[s[1]](s[0],s[2])
        return int(s)

    def find_inner_paren(self, s):
        lp, rp = 0, 0
        for e,c in enumerate(s):
            if c == '(': lp = e
            if c == ')':
                rp = e
                break
        return lp, rp


from operator import mul,truediv,add,sub

class Calculator:
    def __init__(self):
        self.res = list()
        self.op = {
                '+' : add,
                '-' : sub,
                '*' : mul,
                '/' : truediv,
                }

    def evaluate(self, s):
        self.res = s.split()
        self.counter(['*','/'])
        self.counter(['+','-'])
        return float(self.res[0])

    def counter(self, ops):
        i = 1
        while i != len(self.res):
            if self.res[i] in ops:
                self.res[i-1] = str(self.op[self.res[i]](float(self.res[i-1]), float(self.res[i+1])))
                self.res.pop(i+1)
                self.res.pop(i)
                continue
            i += 1



print(Calculator().evaluate("2 / 2 + 3 * 4 - 6")) # => 7
print(Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )"))
print(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"))
#print(Calculator().op['+'](1,2))

















"""
Plan:
    PEMDAS = Parentheses, exponents,
    multiplication & division, addition & subtraction


"""
