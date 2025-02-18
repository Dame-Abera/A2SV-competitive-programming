# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        arr=[0]
        count=0
        for i in  range(len(nums)):
            arr.append(arr[-1]+nums[i])  
        deck=defaultdict(int)
        for i  in arr:
            if i-goal in deck:
                count+=deck[i-goal]
            deck[i]+=1   
        return count

