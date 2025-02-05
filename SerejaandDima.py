n=int(input())
lst=list(map(int,input().split()))
sereja=dima=0
 
left=0
right=n-1
role=True
while left<=right:
    if role:
        if lst[left]>lst[right]:
            sereja+=lst[left]
            left+=1
        else:
            sereja+=lst[right]
            right-=1
            
        role=False
    else:
        if lst[left]>lst[right]:
            dima+=lst[left]
            left+=1
        else:
            dima+=lst[right]
            right-=1
            
        role=True
print(sereja,dima)
