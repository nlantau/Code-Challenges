# nlantau, 2021-12-28

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        return Counter(nums).most_common()[-1][0]



Solution().singleNumber([2,2,1])
Solution().singleNumber([4,1,2,1,2])
Solution().singleNumber([1])

assert Solution().singleNumber([2,2,1]) == 1
assert Solution().singleNumber([4,1,2,1,2]) == 4
assert Solution().singleNumber([1]) == 1

"""
Notes:
116 ms, 16.8 MB, 99.42% faster
"""







