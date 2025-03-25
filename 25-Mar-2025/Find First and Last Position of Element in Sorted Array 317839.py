# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l=0
        r=len(nums)-1
        while r>=l:
            mid=(r+l)//2
            print(mid)
            if nums[mid]==target:
                nr=mid
                nl=mid
                print("get")
                while nl>0 and  nums[nl-1]==target:
                    nl-=1
                    print("w")
                while  nr<len(nums)-1 and  nums[nr+1]==target:
                       nr+=1
                       print("s")
                print(nl,nr,mid)  
                return  [nl,nr]    
                
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1   
        return [-1,-1]            
                     