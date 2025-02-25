# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1=l1
        h2=l2
        prev1=None
        prev2=None
        ans=ListNode(0)
        a=ans
        while h1 and h2:
            nxt1=h1.next
            h1.next=prev1
            prev1=h1
            h1=nxt1
            nxt2=h2.next
            h2.next=prev2
            prev2=h2
            h2=nxt2
        while h1:  
            nxt1=h1.next
            h1.next=prev1
            prev1=h1
            h1=nxt1
        while h2:
            nxt2=h2.next
            h2.next=prev2
            prev2=h2
            h2=nxt2  
        total1=0
        total2=0

        while prev1:
            total1=total1*10+prev1.val
            prev1=prev1.next

        while prev2:
            total2=total2*10+prev2.val
            prev2=prev2.next    
        sum=total1+total2
        print(sum)


        print(prev1)
        print(prev2)
        if sum==0:
            return ans
        while sum:
            curr=sum%10
            newnode=ListNode(curr)
            a.next=newnode
            a=a.next
            sum//=10
        return ans.next    

        
          
