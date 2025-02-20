# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=0
        dummy=ListNode(0,head)
        while curr:
            count+=1
            curr=curr.next
        pt=count-n
        curr=dummy
        s=0
        while  count and curr and curr.next:    
            if s==pt:
              curr.next=curr.next.next
            curr=curr.next
            s+=1
        return dummy.next