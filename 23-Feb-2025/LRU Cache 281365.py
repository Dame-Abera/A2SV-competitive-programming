# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self,key,val):
        self.val=val
        self.next=None
        self.prev=None
        self.key=key
class LRUCache:
    def __init__(self, capacity: int):
        self.cache={}
        self.right=Node(0,0)
        self.left=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        self.cap=capacity
    def add(self,node):
        a=self.right
        b=self.right.prev
        new=node
        new.next=a
        new.prev=b
        a.prev=new
        b.next=new
    def  pop(self,node): 
        a=node.next
        b=node.prev
        b.next=a
        a.prev=b
    def get(self, key: int) -> int:
        if key in self.cache:
            lru=self.cache[key] 
            self.pop(lru)
            self.add(lru)
            return lru.val  
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:    
            self.pop(self.cache[key])
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add(self.cache[key])
        if len(self.cache) > self.cap:
            lr=self.left.next
            print(self.left)
            self.pop(lr)
            print(lr)
            del self.cache[lr.key]
            



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)