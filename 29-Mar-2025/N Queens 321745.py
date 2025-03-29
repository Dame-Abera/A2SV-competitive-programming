# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for i   in range(n)]

        print(board)
        res=[]
        main1=set()
        main2=set()
        cols=set()
        def backtrack(row):
            if row==n:
                res.append(["".join(i) for i  in board])
                return 
            for col  in range(n):
                if col in   cols or col-row in main1 or col+row in main2:
                    continue
                main1.add(col-row)  
                main2.add(col+row) 
                cols.add(col) 
                board[row][col]="Q"
                backtrack(row+1)
                main1.remove(col-row)  
                main2.remove(col+row) 
                cols.remove(col)
                board[row][col]="."


        backtrack(0)
        return res
        