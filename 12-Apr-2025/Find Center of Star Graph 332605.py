# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        deck=defaultdict(list)
        for a,b   in edges:
              deck[a].append(b)
              deck[b].append(a)
        for i in deck:
            if len(deck[i])==len(edges):
                return i     