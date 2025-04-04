# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod=10**9+7
        idx={}
        nums=[]
        for i,val  in enumerate(instructions):
              idx[i]=[0,0]
              nums.append((val,i))   
        def mergesort(nums):
                nonlocal idx
                
                if len(nums)<=1:
                    return nums
                mid=len(nums)//2
                left=mergesort(nums[:mid])
                right=mergesort(nums[mid:])
                r=0
                l=0
                keys = [x[0] for x in left]
                for i   in right:
                    
                    l=bisect_left(keys,i[0])
                    r=bisect_right(keys,i[0])
                    
                    end=len(left)-r
                    idx[i[1]][0]+=l
                    idx[i[1]][1]+=end
                   

                return merge(left,right)
        def merge(left,right):      
                res=[]
                i,j=0,0
                while i<len(left) and j<len(right):
                    if left[i][0]>=right[j][0]:
                            res.append(right[j])
                            j+=1
                    else:
                        res.append(left[i])
                        i+=1
            
                res.extend(left[i:])
                res.extend(right[j:])
                return res
        mergesort(nums)        
        ans=0
        for i  in idx:
            ans+=min(idx[i])       
        return ans%mod


        