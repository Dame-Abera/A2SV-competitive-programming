# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything,  modify board in-place instead.
        """
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        def inbound(r,c):
            return 0<=r<len(board) and 0<=c<len(board[0])
        def dfs(visited,r,c):
            visited.add((r,c))
            
            for rc,cc  in dir:
                nr=rc+r
                nc=cc+c
              
                if inbound(nr,nc) and board[nr][nc]=="O"  and (nr,nc) not in visited:
                    dfs(visited,nr,nc)
        for r  in range(len(board)):
            for c in range(len(board[0])):
                 visited=set()
                 if board[r][c]=="O":
                    dfs(visited,r,c)
                 row=[i[0]  for i  in visited]
                 col=[i[1] for i  in visited]
                 if 0 in row or len(board)-1 in row or 0 in col or len(board[0])-1 in col:
                    continue
                 else:   

                       for a,b in visited:
                        board[a][b]="X"
                            