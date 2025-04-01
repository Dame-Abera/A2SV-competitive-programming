# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        arr=[]
        a=c.values()
        a=sorted(a)
        a=a[::-1]
        b=a[:k]
        for i in c:
            if c[i]   in b:
                arr.append(i) 
        return arr