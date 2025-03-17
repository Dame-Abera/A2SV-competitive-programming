# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):    
    #         self.level=0
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # q=deque([root])
        # print(q)
        # i=0
        # while q:
        #     if i%2:    
        #         l=0
        #         r=len(q)-1
        #         while r>=l:
        #             q[l].val,q[r].val=q[r].val,q[l].val
        #             r-=1
        #             l+=1
        #     for _ in range(len(q)):
        #             temp=q.popleft()
        #             if temp.left:
        #               q.append(temp.left)
        #             if temp.right:
        #                 q.append(temp.right)
        #     i+=1            
        # return root                
                        
        self.dfs(root.left,root.right,1)    
        return root   
    def dfs(self,left,right,level):
        if not left:  
            return  
        else:
            if  level%2 and left:
                left.val,right.val=right.val,left.val   
            self.dfs(left.left,right.right,level+1) 
            self.dfs(left.right,right.left,level+1)
            
         
        
                