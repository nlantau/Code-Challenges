# nlantau, 2022-01-12

"""
Easy one. They got me on a couple of stupid mistakes; Didn't check
empty stack nor length of stack
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: return False

        stack = []

        for c in s:
            if c == "(": stack.append(c)
            elif c == "[": stack.append(c)
            elif c == "{": stack.append(c)

            elif c == ")":
                if len(stack) > 0:
                    t = stack.pop()
                    if t != "(": return False
                else: return False

            elif c == "]":
                if len(stack) > 0:
                    t = stack.pop()
                    if t != "[": return False
                else: return False

            elif c == "}":
                if len(stack) > 0:
                    t = stack.pop()
                    if t != "{": return False
                else: return False

        if len(stack) > 0: return False
        return True

"""
Notes:
Ugly AF, but it works.
42 ms, 29.40% faster, 14.5MB, 7.59% better
"""


if __name__ == "__main__":
    s = "()" # true
    print(Solution().isValid(s))

    s = "()[]{}" # true
    print(Solution().isValid(s))

    s = "(]" # false
    print(Solution().isValid(s))

    s = "((" # false
    print(Solution().isValid(s))

    s = "){" # false
    print(Solution().isValid(s))

