#!/usr/bin/python3

import re


def top_3_words(t):
    t = t.lower()
    #m = re.compile(r"\'?[a-z]{1,}\'?[a-z]{0,}|[a-z]{1,}\'?\'?[a-z]{1,}\'?|[a-z]\'[a-z]{1,}\'[a-z]{1,}")
    m = re.compile(r"\'?[a-z]{1,}\'?[a-z]{0,}|[a-z]{1,}\'\'[a-z]{1,}\'?")

    wl = m.findall(t)

    wd = dict()

    for w in wl:
        if w not in wd.keys():
            wd[w] = 1
        else:
            wd[w] += 1

    wd2 = {k:v for k,v in sorted(wd.items(), key=lambda item: item[1])}

    fl = list()
    for k,v in wd2.items():
        fl.append(k)

    return fl[:-4:-1]




if __name__ == "__main__":
    print(top_3_words(" //wont won't won't"))
    print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
    #print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
    #mind, there lived not long since one of those gentlemen that keep a lance
    #in the lance-rack, an old buckler, a lean hack, and a greyhound for
    #coursing. An olla of rather more beef than mutton, a salad on most
    #nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
    #on Sundays, made away with three-quarters of his income."""))
    print(top_3_words("  '  "))

