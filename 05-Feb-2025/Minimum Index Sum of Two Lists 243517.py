# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap=defaultdict(int)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    if list1[i] in hashmap:
                         hashmap[list1[i]]=min(hashmap[list1[i]],i+j)
                    else:
                        hashmap[list1[i]]=i+j
        mylist=list(hashmap.values()) 
        minv=min(mylist) 
        res=[]  
        for i in hashmap:
            if   hashmap[i]==minv:
                res.append(i)  
        return res
        print(res)               

