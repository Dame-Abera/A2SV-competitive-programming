# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap=[]
        heapq.heapify(heap)
        for i  in range(len(grid)):
            grid[i].sort(reverse=True)
        for  i  in range(len(grid)):
            cand=grid[i][:limits[i]]
            for j in cand:
                if len(heap)<k:
                    heapq.heappush(heap,j)
                else:
                    if heap:
                            s=heapq.heappop(heap) 
                            if s>j:
                                heapq.heappush(heap,s)   
                            else:
                                heapq.heappush(heap,j)  
                    

        return sum(heap)