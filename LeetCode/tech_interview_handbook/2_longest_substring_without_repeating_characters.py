# nlantau, 2022-02-04

"""
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        temp = ""


        for i in range(len(s)-1):

            for j in range(i+1, len(s)):
                pass




s = "abcabcbb"
Solution().lengthOfLongestSubstring(s)
print("-<<<----->>>-")
s = "bbbbb"
Solution().lengthOfLongestSubstring(s)
print("-<<<----->>>-")
s = "pwwkew"
Solution().lengthOfLongestSubstring(s)
