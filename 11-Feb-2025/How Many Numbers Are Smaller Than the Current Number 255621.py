# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=sorted(nums)
        hmap=defaultdict(list)
        c=0
        res=[]
        for i in temp:
            hmap[i].append(c)
            c+=1
        for j in nums:
            res.append(hmap[j][0])
        print(hmap)  
        print(res)  
        return res
