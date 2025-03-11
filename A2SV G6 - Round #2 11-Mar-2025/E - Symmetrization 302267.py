# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

s=int(input())
mat=[]
temp=[]
ones=0
count=0
for _ in range(s):
    n=int(input())
    mat=[]
    count=0
    for s in range(n):
        line=input()
        mat.append([int(t) for t in line])
    for i in range((n+1)//2):
        for j in range(i,n-i-1):
            ones=0
            ones+=mat[i][j]
            ones+=mat[j][n-1-i]
            ones+=mat[n-1-i][n-j-1]
            ones+=mat[n-1-j][i]  
            count+=min(ones,4-ones)
    print(count)

