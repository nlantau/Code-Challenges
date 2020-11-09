# nlantau, 2020-11-09
"""
Trolls are attacking your comment section!
A common way to deal with this situation is to remove
all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a
string and return a new string with all vowels removed.

For example, the string
"This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""
vov = {"a", "e", "i", "o", "u"}


def disemvowel(s):
    return "".join(
        ["".join(i) for i in s if i.lower() not in {"a", "e", "i", "o", "u"}]
    )


print(disemvowel("ThisThis website is for losers LOL! "))