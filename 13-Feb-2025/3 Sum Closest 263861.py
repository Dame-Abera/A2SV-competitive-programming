# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        cl=float("inf")
        res=sum(nums[:3])
        for i in range(len(nums)-2):
            r,l=len(nums)-1,i+1
            while r>l:
                s=nums[l]+nums[r]+nums[i]
                
                if    s==target:
                    return   s
                elif s>target:
                    r-=1
                else:
                    l+=1
                if   abs(target-s)<cl:
                    cl= abs(target-s)
                    print(cl,res)
                    res=s
        return  res     
