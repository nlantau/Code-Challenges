# nlantau, 2020-10-29
"""
The goal of this exercise is to convert a string to a new string where
each character in the new string is "(" if that character appears only
once in the original string, or ")" if that character appears more
than once in the original string. Ignore capitalization when determining
if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
Notes

Assertion messages may be unclear about what they display in some languages.
If you read "...It Should encode XXX",
the "XXX" is the expected result, not the input!

')o()((((j(((' should equal ')(()(((((((('

'))()j(()))gq()p())()))(' should equal '))()((()))((()(())()))('

'))qt)))g))otr)()))ro(g)))()q)p()))hi' should equal '))))))))))))))()))))())))()))(()))(('

'(ho(((s(i(tj(((' should equal '((((((((((((((('

'((((((' should equal ')))))('
"""


def duplicate_encode(word):
    word = word.lower()
    return "".join("(" if word.count(x) == 1 else ")" for x in word)


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
print(duplicate_encode("(ho(((s(i(tj((("))
print(duplicate_encode("))qt)))g))otr)()))ro(g)))()q)p()))hi"))
print(duplicate_encode("(((((("))
