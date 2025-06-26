# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z="0"
        a=""
        b=""
        count=0
        while x>0:
            s=x%2
            a+=str(s)
            x=x//2
        print(a)  
        while y>0:
            s=y%2
            b+=str(s)
            y=y//2
        
        b=b[::-1]
        a=a[::-1]
        if  len(a)>len(b):
            l=len(a)-len(b)
            b="0"*l+b
        else:   
            l=len(b)-len(a)
            a="0"*l+a
        for  i  in  range(max(len(a),len(b))):
             if a[i]!=b[i]:
                count+=1
        print(a,b)        
        return  count        

