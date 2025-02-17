# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B


n,k,q=map(int,input().split())
que=[]
bound=0

for _  in  range(n):
  l,r=map(int,input().split())
  bound=max(bound,l,r)
  que.append([l,r])
arr=[0]*(200002)

for a in que:
   arr[a[0]] += 1
   arr[a[1] + 1] -= 1

for i  in  range(1,len(arr)):
   arr[i]=arr[i]+arr[i-1]

count=0
for  j in range(len(arr)):
   if arr[j]>=k:
      arr[j]=1
   else:
      arr[j]=0
for k  in range(1,len(arr)):
   arr[k]=arr[k-1]+arr[k]
for _ in range(q):
    l,r=map(int,input().split())
    count=arr[r]-arr[l-1]
    print(count)
     