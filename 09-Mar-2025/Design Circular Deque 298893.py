# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class Node:
    def __init__(self,val):
        self.next=None
        self.val=val
        self.prev=None

class MyCircularDeque:
        
    def __init__(self, k: int):
        self.k=k
        self.left=Node(-1)
        self.right=Node(-1)
        self.left.next=self.right
        self.right.prev=self.left
        self.count=0
    def insertFront(self, value: int) -> bool:
        if self.count==self.k:
            return False
        newn=Node(value)
        a=self.left.next
        b=self.left
        newn.next=a
        newn.prev=b
        b.next=newn
        a.prev=newn
        self.count+=1
        

        return True
        
    def insertLast(self, value: int) -> bool:
        if self.count==self.k:
            return False
        newn=Node(value)   
        a=self.right
        b=self.right.prev
        newn.next=a
        newn.prev=b
        a.prev=newn
        b.next=newn
        self.count+=1
       
        return True
        
    def deleteFront(self) -> bool:
        if self.count==0:
            return False 
        nxt=self.left.next.next 
        b=self.left
        self.left.next=nxt
        nxt.prev=b
        self.count-=1
        
        return True    

    def deleteLast(self) -> bool:
        print(self.count)
        if self.count==0:
            return False
        b=self.right.prev.prev
        a=self.right
        b.next=self.right
        self.right.prev=b
        self.count-=1     
        return True  
    def getFront(self) -> int:
        return self.left.next.val

    def getRear(self) -> int:
        return self.right.prev.val

    def isEmpty(self) -> bool:
        if self.count==0:
            return True
        else:
            return False    

    def isFull(self) -> bool:
        if self.k==self.count:
            return True
        else:
            return False    


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()