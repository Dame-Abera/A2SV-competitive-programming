# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left=ListNode(0)
        
        curr=head
        while curr:
           new=ListNode(curr.val)
           place=left.next
           new.next=place
           left.next=new
           
           curr=curr.next
        return left.next
