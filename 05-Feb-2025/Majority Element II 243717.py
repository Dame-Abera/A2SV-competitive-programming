# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        n=len(nums)
        arr=[]
        for i in c:
            if c[i]>n/3:
                arr.append(i)
        return arr        