# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rabbit=head
        tortoise=head
        while rabbit and rabbit.next:
            rabbit=rabbit.next.next
            tortoise=tortoise.next    
            if rabbit==tortoise:
                break
           
        else:
            return   
        tortoise=head
        while rabbit!=tortoise:
            rabbit=rabbit.next
            tortoise=tortoise.next
        return tortoise    