# nlantau, 2022-01-29

from typing import *

class Solution:
    pass

class NumArray:
    """
    Your NumArray object will be instantiated and called as such:
    obj = NumArray(nums)
    param_1 = obj.sumRange(left,right)
    """

    def __init__(self, nums: List[int]):
        self.arr = nums

    def sumRange(self, left: int, right: int) -> int:
        """
        Notes: 5796 ms, 13.44% faster, 17.5 MB, 91.64% better
        """
        res = 0
        print("nums: ", self.arr)
        for i in range(left, right + 1, 1):
            res += self.arr[i]
            print(res, end=', ')
        return res


class TestClass:
    def test_example_2(self):
        arr = [-2,0,3,-5,2,-1]
        num_arr = NumArray(arr)
        assert num_arr.sumRange(0,2) == 1

    def test_example_3(self):
        arr = [-2,0,3,-5,2,-1]
        num_arr = NumArray(arr)
        assert num_arr.sumRange(2,5) == -1

    def test_example_4(self):
        arr = [-2,0,3,-5,2,-1]
        num_arr = NumArray(arr)
        assert num_arr.sumRange(0,5) == -3


if __name__ == "__main__":
    arr = [-2,0,3,-5,2,-1]
    num_arr = NumArray(arr)
    print("->", num_arr.sumRange(0,2))
    print("->", num_arr.sumRange(2,5))
    print("->", num_arr.sumRange(0,5))
