# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr=[]
        for idx,val in enumerate(nums):
             arr.append([0,idx])
        for a,b in requests:
            arr[a][0]+=1
            if b<len(arr)-1:
                 arr[b+1][0]-=1
        for i in range(1,len(arr)):
            arr[i][0]=arr[i-1][0]+arr[i][0] 
        arr.sort(key= lambda a:a[0],reverse=True)
        nums.sort(reverse=True)
        res=[0]*len(nums)
        
        for  i in range(len(nums)):
            res[arr[i][1]]=nums[i]
        ans=0    
        print(res)
        print(arr)
        for  req  in arr:
             ans+=res[req[1]]*req[0]
        print(ans)     
        return ans%1000000007


