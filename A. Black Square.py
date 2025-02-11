n=list(map(int,input().split()))
s=input()
a=len(s)
res=0
for i in range(a):
    b=int(s[i])
    res +=n[b-1]
print(res)
