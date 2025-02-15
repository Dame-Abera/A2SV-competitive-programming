# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.arr=[0]
        for i in range(len(self.nums)):
            self.arr.append(self.nums[i]+self.arr[-1])
       
    def sumRange(self, left: int, right: int) -> int:
       
        return self.arr[right+1]-self.arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)