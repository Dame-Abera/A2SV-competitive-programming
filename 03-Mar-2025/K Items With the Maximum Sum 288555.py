# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        tot=0
        if k<=numOnes:
            tot=k
        
        elif k<=numOnes+numZeros:
            tot=numOnes
        else:
            tot=numOnes-(k-numOnes-numZeros)       
        print(tot)    
        return tot

            

