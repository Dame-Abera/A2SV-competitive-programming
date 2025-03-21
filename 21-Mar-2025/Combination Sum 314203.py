# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def dfs(start,path):
            
            if sum(path)==target and sorted(path) not in ans:
                ans.append(sorted(path[:]))
                return
            if sum(path)>target:
                return   
            for  i in range(len(candidates)):
                path.append(candidates[i])
                
                dfs(i+1,path)
                path.pop()
        dfs(0,[])   
        return   ans   
                     

