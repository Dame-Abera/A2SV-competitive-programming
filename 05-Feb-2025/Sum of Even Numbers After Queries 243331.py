# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evensum=0
        arr=[]
        for i in nums:
            if i%2==0:
                evensum+=i
        print(evensum)        
        for val,idx in queries:
            if nums[idx]%2==0:
                evensum-=nums[idx]
            nums[idx]+=val
            print(evensum)
            if nums[idx]%2==0:
                evensum+=nums[idx]
          
            arr.append(evensum)
        return arr    