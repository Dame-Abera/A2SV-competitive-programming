# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        arr=[]
        for i in c:
            if c[i]==2:
                arr.append(i)
        return arr        
