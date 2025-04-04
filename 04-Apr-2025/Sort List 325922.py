# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r=head
        res=[]
        ans=ListNode(0)
        a=ans
        while r:
            res.append(r.val)
            r=r.next
        res.sort()
        for i  in res:
            a.next=ListNode(i)
            a=a.next
        return ans.next    
             

