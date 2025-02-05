# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        hashmap={}
        for i in range(len(s)):
            hashmap[indices[i]]=s[i]
        mylist=list(hashmap.keys())
        mylist.sort()
        res=[]
        for i in mylist:
            res.append(hashmap[i])
        return "".join(res)