# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l=0
        r=len(citations)-1
        ans=0
        while r>=l:
            mid=(r+l)//2
            if citations[mid]>=len(citations)-mid:
                ans=len(citations)-mid 
                r=mid-1
            else:
                l=mid+1

        return ans       