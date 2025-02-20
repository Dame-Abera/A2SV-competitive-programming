# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=ListNode(0)
        curr=head
        lmover=l
        hset=set()
        while curr:
            if curr.val not  in hset:
                lmover.next=curr
                lmover=lmover.next
            hset.add(curr.val)
            print(hset)
            curr=curr.next
        lmover.next=None    
        return  l.next