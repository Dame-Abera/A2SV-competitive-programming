# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod=10**9+7
        res=0
        stack=deque()
        n=len(arr)
        forward=[n]*n
        backward=[-1]*n
        rev=arr[::-1]
        for i,v  in enumerate(arr):
            while stack and arr[stack[-1]]>v:
                   forward[stack[-1]]=i
                   stack.pop()
            stack.append(i)       
        stack=deque()
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                backward[stack[-1]]=i
                stack.pop()
            stack.append(i)
          
        for i,v  in enumerate(arr):
            res+=v*(forward[i]-i)*(i-backward[i])





        return res%mod