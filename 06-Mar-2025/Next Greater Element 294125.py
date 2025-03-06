# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        deck={}
        stack=deque()
        
        for i  in nums2:
            deck[i]=-1
        print(deck)    
        for i in nums2:
            while stack and stack[-1]<i:
                a=stack.pop()
                deck[a]=i
            stack.append(i)    
        for i,v in enumerate(nums1):
            nums1[i]=deck[v]
        return nums1    