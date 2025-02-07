# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res=[[0 for i in range(len(img[0]))] for j in range(len(img))]
        tot=0
        rlim=len(img)-1
        clim=len(img[0])-1
        for row in range(len(img)):
            for col in range(len(img[0])):
                size=0
                t0t=0
                tot+=img[row][col]
                size+=1
                # 2
                if row-1>=0 and col-1>=0:
                    tot+=img[row-1][col-1]
                    size+=1
                # 3
                if row-1>=0:
                    tot+=img[row-1][col]
                    size+=1
                #4 
                if col+1<=clim and row-1>=0:
                    tot+=img[row-1][col+1]
                    size+=1
                # 5
                if col+1<=clim:
                    tot+=img[row][col+1] 
                    size+=1
                #6
                if col+1<=clim and row+1<=rlim:
                    tot+=img[row+1][col+1] 
                    size+=1  
                #7
                if row+1<=rlim:
                    tot+=img[row+1][col]  
                    size+=1
                #8    
                if  row+1<=rlim and col-1>=0:
                    tot+=img[row+1][col-1]
                    size+=1
                #9    
                if col-1>=0:
                    tot+=img[row][col-1] 
                    size+=1  

                res[row][col]=floor(tot/size)
                tot=0
                size=0
        return res
