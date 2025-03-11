# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        hash={0:1,1:1}
        temp={0:1,1:1}
        if rowIndex==0:
            return [1]
        if   rowIndex==1:
            return [1,1] 
        for i in range(1,rowIndex):
            for j  in range(1,i+1):
                temp[j]=hash[j-1]+hash[j]
            temp[i+1]=1 
            hash=copy.deepcopy(temp) 
           
        res=[]
        ntemp=sorted(hash.keys())
        for i  in ntemp:
            res.append(hash[i])
        
        return res

