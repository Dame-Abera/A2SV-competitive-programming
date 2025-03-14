# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def __init__(self):
        self.s=float("-inf")
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        if self.predictWinner(nums,0,len(nums)-1)>=0:
          return True
        else:
          return False   
    def predictWinner(self,nums,l,r):
        if r==l:
            return nums[l]
        winnerselectsright=nums[r]-self.predictWinner(nums,l,r-1)
        winnerselectsleft=nums[l]-self.predictWinner(nums,l+1,r)  
        #comment
        self.s=max(winnerselectsright,winnerselectsleft)
        return self.s
               

           
