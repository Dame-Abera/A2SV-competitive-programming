# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        ct=Counter(s)
        arr=[]
        res=""
        for  i  in ct:
            arr.append([ct[i],i])
        arr.sort(key=lambda a:a[0] ,reverse=True)    
        print(arr)
        for j in arr:
             res+=j[1]*(j[0])
        return res     