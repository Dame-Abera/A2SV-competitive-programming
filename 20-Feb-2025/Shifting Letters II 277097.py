# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr=[0]*(len(s) +1)
        res=[]
        for i in s:
            res.append(ord(i)-ord("a"))  
        for start,end,di in shifts:
            if di==0:
                arr[start]-=1
                arr[end +1]+=1
            else:
                arr[start]+=1
                arr[end+1]-=1
        
        for j   in  range(1,len(arr)):
            arr[j]=arr[j]+arr[j-1]
        print(arr) 
        for  k in range(len(res)):
            res[k]+=arr[k]
        for l  in range(len(res)):
            res[l]=chr(res[l]%26+ord("a"))
        return "".join(res)