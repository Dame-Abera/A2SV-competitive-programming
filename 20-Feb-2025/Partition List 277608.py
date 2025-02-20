# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessthan=ListNode()
        greaterthan=ListNode()
        curr=head
        l=lessthan
        g=greaterthan
        while curr:
            new=ListNode(curr.val)
            if curr.val>=x:
                g.next=new
                g=g.next
            else:
                l.next=new
                l=l.next  
            curr=curr.next
        l=lessthan.next
        g=greaterthan.next
        ans=ListNode()
        aptr=ans
        
        while l:
            aptr.next=l
            aptr=aptr.next
            l=l.next
        while g:
            aptr.next=g
            aptr=aptr.next
            g=g.next  
        return ans.next  