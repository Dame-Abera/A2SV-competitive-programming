# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left=ListNode(0)
        curr=head
        while curr:
            new=ListNode(curr.val)
            place=left.next
            new.next=place
            left.next=new
            curr=curr.next
        curr=head
        left=left.next
        while curr:
            
            if left.val!=curr.val:
                return False
            curr=curr.next
            left=left.next    
        return True     
            
