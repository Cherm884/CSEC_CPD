n = int(input())
check='2'
ans=1
 
for i in range(n):
    a= input()
 
    if a[0]==check:
        ans+=1
    check=a[-1]
    
print(ans)
