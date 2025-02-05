# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        self.numlist=[]
        self.nummap={}

    def insert(self, val: int) -> bool:
        res=val not in self.numlist
        if res:
            self.nummap[val]=len(self.numlist)
            self.numlist.append(val)
        return res   
    def remove(self, val: int) -> bool:
        res=val in self.numlist
        if res:
            idx=self.nummap[val]
            lstidx=len(self.numlist)-1
            lst=self.numlist[lstidx]
            self.numlist[lstidx],self.numlist[idx]=val,self.numlist[lstidx]
            self.nummap[lst]=idx
            self.nummap[idx]=lstidx
            del self.nummap[val]
            self.numlist.pop()
        return res        
    def getRandom(self) -> int:
        return choice(self.numlist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()