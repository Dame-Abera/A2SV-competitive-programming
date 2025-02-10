# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for  idx,val  in enumerate(nums):
            nums[idx]=str(val)
        def  helper(n1,n2):
            if n1+n2>n2+n1:
                return -1
            else:
                return 1
        ans=sorted(nums,key=cmp_to_key(helper)) 
        print(ans)
        return str(int("".join(ans)))
