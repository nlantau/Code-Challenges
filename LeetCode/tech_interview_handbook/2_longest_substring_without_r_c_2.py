# nlantau, 2022-01-05

"""
Given a string s, find the length of the longest substring
without repeating characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_set = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in sub_set:
                sub_set.remove(s[left])
                left += 1
            sub_set.add(s[right])
            res = max(res, len(sub_set))
        return res

"""
Notes:
64 ms, 67.94% faster, 14.5 MB, 6.65% better
"""

if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
    s = "bbbbb"
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1

    print(Solution().lengthOfLongestSubstring("pwwkew"))
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    print(Solution().lengthOfLongestSubstring("pwwkew"))


