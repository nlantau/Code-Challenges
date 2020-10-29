"""
'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false


Write function:
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""


def anagrams(word_to_match: str, word_list: list) -> list:
    return [word for word in word_list if sorted(word_to_match) == sorted(word)]


print(anagrams("abba", ["aabb", "abcd", "bbaa", "dada"]))

print(anagrams("racer", ["crazer", "carer", "racar", "caers", "racer"]))
