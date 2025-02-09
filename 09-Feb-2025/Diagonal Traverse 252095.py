# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        arr=[]
        clim=len(mat[0])-1
        rlim=len(mat)-1
        res=[]
        temp=[]
        flag=True
        for i  in range(len(mat)):
            col=0
            row=i
            temp=[]
            while col<=clim and row>=0:
                temp.append(mat[row][col])
                col+=1
                row-=1    
            if flag:
                for k in temp:
                    res.append(k)
                flag=False    
            else:
               
                temp=temp[::-1] 
               
                for k in temp:
                    res.append(k) 
                flag=True        
        for j in range(1,len(mat[0])):
            col=j
            row=rlim
            temp=[]
           
            while col<=clim  and row>=0:
              
                temp.append(mat[row][col])   
                col+=1
                row-=1
             
            if flag:
                for k in temp:
                    res.append(k)
                flag=False    
            else:
                temp=temp[::-1] 
                for k in temp:
                    res.append(k)    
                flag=True         
           
        return res            