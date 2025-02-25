# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        h1=head
        l=0
        while h1:
            l+=1
            h1=h1.next
        h=l//2
        h1=head
        while h:
            prev=h1
            h1=h1.next
            h-=1    
        dummyNode=ListNode(0)
        d=dummyNode
        r=d.next
        while h1:
            new=ListNode(h1.val)
            new.next=r
            d.next=new
            r=new
            h1=h1.next
        d=dummyNode.next
        maxval=float("-inf")
        h1=head
        while h1 and  d:
            maxval=max(maxval,h1.val+d.val)  
            h1=h1.next
            d=d.next 
        return maxval    