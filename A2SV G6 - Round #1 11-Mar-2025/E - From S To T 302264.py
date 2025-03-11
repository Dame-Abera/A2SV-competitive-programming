# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

n=int(input())                 
for i in range(n):
    s=input()
    t=input()
    p=input()
    arr=list(p)     
    temp=[]
    j=0
    for  char  in t:
        if j<len(s)  and char==s[j]:
            temp.append(char)
            j+=1
        elif char in arr:
                temp.append(char)
                arr.remove(char)
    if j<len(s):
         print("NO") 
    else:     
        if "".join(temp)==t:
           print("YES")
        else:
            print("NO")
    