# nlantau, 2021-10-27

"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

import re

def pig_it(t):
    rec = re.compile(r'[a-zA-Z]')
    t = t.split()
    temp = ''
    for i, w in enumerate(t):
        if rec.match(w):
            temp = w[0]
            t[i] = w[1:] + temp + 'ay'
    return " ".join(t)


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))
print(pig_it('This is my string'))
