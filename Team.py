n=int(input())
res=0
for i in range(n):
    a,b,c=map(int,input().split())
    if a+b+c >=2:
        res +=1
print(res)
