# Problem: Candy - https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        arr=[]
        n=len(ratings)
        candy=[1]*len(ratings) 
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candy[i]=candy[i-1]+1
        for i   in range(n-1,-1,-1):
            if i==n-1:
                continue
            if ratings[i]>ratings[i+1]:
                  candy[i]=max(candy[i+1]+1,candy[i])   
        
        return sum(candy)                       


              