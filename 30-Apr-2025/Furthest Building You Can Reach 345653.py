# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        heapq.heapify(heap)
        res=0
        for i  in range(1,len(heights)):
            
            if heights[i]>heights[i-1]:
                if len(heap)<ladders:
                    heapq.heappush(heap,heights[i]-heights[i-1])
                else:
                    if heap:
                            s=heapq.heappop(heap)
                            
                            if s>heights[i]-heights[i-1]:
                                heapq.heappush(heap,s)
                                res+=heights[i]-heights[i-1]
                            else:
                                heapq.heappush(heap,heights[i]-heights[i-1])
                                res+=s
                    else:
                        res+=heights[i]-heights[i-1]
            if res>bricks:
                 return i-1            
           
        return len(heights)-1  
                  