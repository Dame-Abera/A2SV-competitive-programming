# Problem: Books - https://codeforces.com/contest/279/problem/B

n,b=map(int,input().split())
arr=list(map(int,input().split()))
book=0
l=0
m=0
for i in range(len(arr)):
    book+=arr[i]
    while  book>b:
        book-=arr[l]
        l+=1
      
    m=max(m,i-l+1)   

print(m)     

