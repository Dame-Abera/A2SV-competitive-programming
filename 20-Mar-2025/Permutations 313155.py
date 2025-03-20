# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return list(list(i) for i  in permutations(nums))
        ans,sol=[],[]
        def  backtrack(arr):
            if   len(arr)==len(nums):
                ans.append(arr[:])
                return
            for cand  in range(len(nums)):
                print(cand)
                print(arr)
                if nums[cand]  not in arr:
                    arr.append(nums[cand])
                    backtrack(arr)    
                    arr.pop()
        backtrack([])
        return  ans