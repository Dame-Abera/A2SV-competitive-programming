# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        # p=heaq.heappop(nums)
        count=0
        while nums[0]<k:
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)
            heapq.heappush(nums,(min(x, y) * 2 + max(x, y)) )
            count+=1
        return count    
            