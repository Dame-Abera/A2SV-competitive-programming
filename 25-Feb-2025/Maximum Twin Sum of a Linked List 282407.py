# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast,slow=head,head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            nxt=slow.next
            slow.next=prev
            prev=slow   
            slow=nxt  
        maxval=float("-inf")
    
        while slow and  prev:
            maxval=max(maxval,prev.val+slow.val)  
            prev=prev.next
            slow=slow.next
        return maxval    