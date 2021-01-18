# nlantau, 2020-12-28

import re


def solution(s, m):
    if len(m) > 1:
        s = s.split("\n")
        r = "[" + "".join(m) + "]"
        print(r)
        print(s)
        com = re.compile(r)
        nl = list()

        for line in s:
            keep = com.search(line)
            if keep:
                print(keep)
                print(keep.span()[0])
                ml = line[: keep.span()[0]].strip(" ")
                print("ml", ml)
                nl.append(ml)
            else:
                nl.append(line)
        print(s)
        nl = "\n".join(nl)
        print(nl)
        return nl
    return s


t_one = "apples, pears # and bananas\ngrapes\nbananas !apples"
t1_cor = "apples, pears\ngrapes\nbananas"
t_two = "a #b\nc\nd $e f g"
t_cor = "a\nc\nd"

if __name__ == "__main__":
    solution(t_two, ["#", "$"])
