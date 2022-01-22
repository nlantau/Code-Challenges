# nlantau, 2022-01-20

from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in hash_table:
                hash_table[sorted_word].append(word)
            else:
                hash_table[sorted_word] = [word]

        print(f'{hash_table=}')

        return list(hash_table.values())
        

class TestClass:
    def test_example_1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        res = Solution().groupAnagrams(strs)
        exp = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
        assert res == exp

    def test_example_2(self):
        strs = [""]
        res = Solution().groupAnagrams(strs)
        exp = [[""]]
        assert res == exp

    def test_example_3(self):
        strs = ["a"]
        res = Solution().groupAnagrams(strs)
        exp = [["a"]]
        assert res == exp

"""
Notes:
156 ms, 29.76% faster, 17 MB, 94.56% better

I initially thought about checked the sorted word, but over-complicated
the matter. Always very clever to use hash tables and should be something
to keep in mind to make use of in general.
"""

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = Solution().groupAnagrams(strs)
    print(res)

