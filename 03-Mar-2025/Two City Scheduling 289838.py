# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
          arr=[]
          n=len(costs)
          res=0
          temp=0
          for i,v in enumerate(costs):
            temp=v[1]-v[0]
            arr.append([temp,i])
          arr.sort(key=lambda a: a[0]) 
          for i in range(n//2):
               res+=costs[arr[i][1]][1]
          for i in range(n//2,n):
               res+=costs[arr[i][1]][0]
          return res   
               