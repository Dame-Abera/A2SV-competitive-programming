# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h={}
        res=[]
        li=0
        for i in range(len(names)):
            h[heights[i]]=names[i]
        mas=max(heights)  
        mis=min(heights)    
        freq=[0]*((mas)+1)
         
        for idx,val  in enumerate(heights):
             freq[val]+=1
        index=0
        for idx,val  in enumerate(freq):
            for value  in range(val):
                heights[index]=idx
                index+=1
        for  l in heights: 
            res.append(h[l])
        return    res[::-1]


