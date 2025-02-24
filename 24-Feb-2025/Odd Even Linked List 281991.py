# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd=ListNode(0)
        even=ListNode(0)
    
        curr=head
        o=odd
        e=even
        flag=True
        while curr:
            new=ListNode(curr.val)
            if flag:
                o.next=new
                o=o.next
            else:
                e.next=new  
                e=e.next 
            curr=curr.next
            flag= not flag
        odd=odd.next
        even=even.next
        o.next=even
        ans=ListNode(0)
        return odd   
        