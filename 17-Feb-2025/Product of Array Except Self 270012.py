# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prepro=[1]
        for i  in range(len(nums)):
            prepro.append(nums[i]*prepro[-1])
        
        
        spro=[1]
        for j in range(len(nums)-1,-1,-1):
            spro.append(spro[-1]*nums[j])
        print(spro)
        spro=spro[::-1]
        res=[]
        for i in range(len(nums)):
            res.append(prepro[i]*spro[i+1])
        return res    
            
        
        
