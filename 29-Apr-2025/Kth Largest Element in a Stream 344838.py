# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        nums=nums[:k]
        print(nums)
        self.heap=nums
        heapq.heapify(self.heap)
        self.k=k
        
    def add(self, val: int) -> int:
       
        if len(self.heap) < self.k:
          heapq.heappush(self.heap, val)
        else:
            min_value = heapq.heappop(self.heap)  
            if min_value<val:
                heapq.heappush(self.heap, val)
            else:
                heapq.heappush(self.heap, min_value)
               
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)