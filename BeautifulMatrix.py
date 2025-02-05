matrix=[[],[],[],[],[]]
n=5
res=0
for i in range(n):
    matrix[i]=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            res=((max(i,2)-min(i,2) )+ (max(j,2)-min(j,2)))
print(res)
 
