# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None
        self.prev=None
class MyLinkedList:
    def __init__(self):
        self.right=Node(0)
        self.left=Node(0)
        self.left.next=self.right
        self.right.prev=self.left
    def get(self, index: int) -> int:
        curr=self.left.next
        while curr  and index>0:
            index-=1
            curr=curr.next
        if curr and self.right!=curr and index==0 :
            return curr.val     
        return -1
    def addAtHead(self, val: int) -> None:
        newnode=Node(val)
        b=self.left
        a=self.left.next
        newnode.next=a
        b.next=newnode
        newnode.prev=self.left
        a.prev=newnode
        
    def addAtTail(self, val: int) -> None: 
        newnode=Node(val)
        b=self.right.prev
        a=self.right
        newnode.next=a
        b.next=newnode
        newnode.prev=b
        a.prev=newnode
       
    def addAtIndex(self, index: int, val: int) -> None:
        curr=self.left.next
        newnode=Node(val)
        while index and curr:
            curr=curr.next
            index-=1
        if curr and index==0:    
            a=curr
            b=curr.prev
            newnode.next=a
            b.next=newnode
            newnode.prev=b
            a.prev=newnode    
    def deleteAtIndex(self, index: int) -> None:
        curr=self.left.next
        while index and curr:
              index-=1
              curr=curr.next
        if curr and index==0  and curr!=self.right:    
            a=curr.next
            b=curr.prev
            b.next=a
            a.prev=b
                   

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.ad
#AtIndex(index,val)
# obj.deleteAtIndex(index)