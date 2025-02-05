# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        n=len(nums)
        arr=[]
        for i in c:
            if c[i]>n/3:
                arr.append(i)
        return arr        
