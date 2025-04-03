# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        initial_sum=sum(nums)
        true_sum=sum(set(nums))
        real_sum=sum(i for i   in range(1,len(nums)+1))
        return  [initial_sum - true_sum,real_sum - true_sum]
