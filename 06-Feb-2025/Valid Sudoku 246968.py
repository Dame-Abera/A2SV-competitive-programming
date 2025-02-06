# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check the row 
        for row in board:
            hashset=set()
            for col in row:
                if col in hashset :
                    print(11)
                    return False
                elif col!=".":
                    hashset.add(col)   
         # check the column            
        i,j=0,0
        hashset=set()
        while i<9:
            hashset=set()
            while j<9:
                if board[j][i] in hashset:
                    print(22)
                    return False
                elif board[j][i]!=".":
                    hashset.add(board[j][i])
                j+=1        
            j=0
            i+=1  
     
    
        #check the 3*3grids
        hashset=set()
        for i in range(3):

            for j in range(3):
                if board[i][j] in hashset :
                    print(33)
                    return False
                elif board[i][j]!=".":
                    hashset.add(board[i][j])
        hashset=set()
        for i in range(3):
            for j in range(3,6):
                if board[i][j] in hashset:
                    print(hashset)
                    return False
                elif  board[i][j]!= "." :
                    hashset.add(board[i][j])    
        
        hashset=set()
        for i in range(3):
            for j in range(6,9):
                if board[i][j] in hashset and board[i][j]!= ".":
                    print(hashset)
                    return False
                elif  board[i][j]!= "." :
                    hashset.add(board[i][j])    
               
        hashset=set()
        for i in range(3,6):
            for j in range(3):
                if board[i][j] in hashset and board[i][j]!= ".":
                    print(hashset)
                    return False
                elif  board[i][j]!= "." :
                    hashset.add(board[i][j])    
                  
        hashset=set()
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j] in hashset and board[i][j]!=".":
                    print(hashset)
                    return False
                    
                elif  board[i][j]!= "." :
                    hashset.add(board[i][j])     
                      
        hashset=set()
        for i in range(3,6):
            for j in range(6,9):
                if board[i][j] in hashset and board[i][j]!=".":
                    print(hashset)
                    return False
                     
                elif  board[i][j]!= "." :
                    hashset.add(board[i][j])    
                
        hashset=set()
        for i in range(6,9):
            for j in range(3):
                if board[i][j] in hashset and board[i][j]!= ".":
                    print(hashset)
                    return False
                elif  board[i][j]!= "." :
                    hashset.add(board[i][j])    
                   
        hashset=set()
        for i in range(6,9):
            for j in range(3,6):
                if board[i][j] in hashset and board[i][j]!= ".":
                    print(hashset)
                    return False
                elif  board[i][j]!= "." :
                    hashset.add(board[i][j]) 
                   
        hashset=set()
        for i in range(6,9):
            for j in range(6,9):
                if board[i][j] in hashset and board[i][j]!=".":
                    print(hashset)
                    return False
                elif  board[i][j]!= "." :
                    hashset.add(board[i][j]) 
                                        
        return True                

