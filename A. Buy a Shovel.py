cost,r = map(int,input().split())
t = cost
res = 1
while True:
    if (cost%10==0) or (cost%10==r):
        break
    res +=1
    cost+=t
print(res)
