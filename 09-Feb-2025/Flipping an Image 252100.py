# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            for j,v in enumerate(image[row]):
                if v==0:
                    image[row][j]=1
                else:
                      image[row][j]=0
        for i in range(len(image)):
            l,r=0,len(image)-1
            while l<=r:
                image[i][l],image[i][r]=image[i][r],image[i][l]
                l+=1
                r-=1       
        return image              