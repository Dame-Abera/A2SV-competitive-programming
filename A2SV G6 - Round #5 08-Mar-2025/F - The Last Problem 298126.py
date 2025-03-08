# Problem: F - The Last Problem - https://codeforces.com/gym/591928/problem/F

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
prefix = [0]
for i in range(n):
    prefix.append(prefix[-1] + a[i] * b[i])
ans = prefix[n] 
for i in range(n):
    prod = a[i] * b[i] 
    l, r = i-1, i +1
    while l >= 0 and r < n:
        prod +=a[r]* b[l]  
        prod +=a[l]* b[r]
        ans = max(ans, prod + prefix[l] + (prefix[-1] - prefix[r+1]))
        l -=1
        r +=1    
    prod = 0
    l, r = i, i+1
    while l >= 0 and r < n:
        prod +=a[r]* b[l]  
        prod +=a[l]* b[r]
        ans = max(ans, prod + prefix[l] + (prefix[-1] - prefix[r+1]))
        l -=1
        r +=1
print(ans)