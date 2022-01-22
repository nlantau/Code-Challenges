# nlantau, 2002-11-08


def spin_words(s):
    # s = s.split(" ")
    # for i, word in enumerate(s):
    # if len(word) >= 5:
    # s[i] = word[::-1]
    # return " ".join(s)
    return " ".join([i[::-1] if len(i) >= 5 else i for i in s.split(" ")])


print(spin_words("hey my name is Niklas Welcome"))