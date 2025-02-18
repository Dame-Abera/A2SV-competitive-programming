# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        arr=[0]
        res=0
        for  i   in  range(len(nums)):
            arr.append(arr[-1]+nums[i])
        deck=defaultdict(int)     
        for i  in range(len(arr)):
            mod=arr[i]%k
            if mod  in  deck:
               res+=deck[mod]
            deck[mod]+=1
        print(deck)     
        return res
           
