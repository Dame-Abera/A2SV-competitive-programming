# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

from collections import defaultdict
n=int(input())
for i in range(n):
    row,col=map(int,input().split())
    chess=[]
    for j in range(row):
        line=list(map(int,input().split()))
        chess.append(line)
    defdec=defaultdict(int)
    for rs in range(row):
        for cs in range(col):
            r,c=rs,cs
            tot=0
            while r<len(chess) and c<len(chess[0]):
                tot+=chess[r][c]
                c+=1
                r+=1
            r,c=rs,cs
            while c>=0 and r>=0:
                tot+=chess[r][c]  
                c-=1
                r-=1
            r,c=rs,cs
            while c<len(chess[0])  and r>=0:
                tot+=chess[r][c]
                c+=1
                r-=1
            r,c=rs,cs
            while r<len(chess) and c>=0:
                tot+=chess[r][c]
                c-=1
                r+=1
            defdec[(rs,cs)]=tot-3*chess[rs][cs]
         
    temp=list(defdec.values())
    print(max(temp))
