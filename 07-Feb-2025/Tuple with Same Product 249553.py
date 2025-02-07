# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count=0
        defdict=defaultdict(list)     
        for  i  in range(len(nums)):
            for j in range(i+1,len(nums)):
                defdict[nums[i]*nums[j]].append((nums[i],nums[j]))      
        for i in defdict:
            temp=defdict[i]
            
            count+=(len(temp)-1)*4*len(nums)
        return count        
        