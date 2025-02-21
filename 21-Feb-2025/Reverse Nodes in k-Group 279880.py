# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=head
        prev=None
        ans=ListNode(0)
       
        a=ans
        while curr:
            less=0
            prev=None
            p=ListNode(0) 
            pp=p
            while curr and less<k:
             pp.next=ListNode(curr.val)
             pp=pp.next
             nxt=curr.next
             curr.next=prev
             prev=curr
             less+=1
             curr=nxt    
            if less==k: 
                a.next=prev
                while a.next:
                    a=a.next  
            else:      
               a.next=p.next
        return ans.next    

            







