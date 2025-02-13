# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res=[]
        def  flip(end):
            start=0
            while start<=end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        for  i in range(len(arr)-1,-1,-1):
            idx=i
            for j in range(i,-1,-1):
                if arr[j]>arr[idx]:
                    idx=j
            if idx!=i:           
                flip(idx)   
                flip(i)  
                res.append(idx+1) 
                res.append(i+1)  
        return   res 

            
            