# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        arr=[0]
        ac=0
        for i in nums:
           ac+=i
           arr.append(ac)
        hmap=defaultdict(int)

        count=0 
    

        for j in arr:
            if j-k in hmap:
                count+=hmap[j-k]
            hmap[j]+=1
        return     count