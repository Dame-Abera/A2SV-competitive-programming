# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr=[]
        self.curr=float("-inf")
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.arr
        q=deque([root])
        print(q)
        
        
        while q:
            self.curr=float("-inf") 
            for _  in range(len(q)):
                temp=q.popleft()
                self.curr=max(self.curr,temp.val)
                if temp.left:

                    q.append(temp.left)
                    

                if temp.right:
                    q.append(temp.right)    
                    
            if self.curr != float('-inf'):
                 self.arr.append(self.curr)    
             
        return self.arr