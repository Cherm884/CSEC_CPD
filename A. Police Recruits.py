events = int(input())
check = list(map(int,input().split()))
crime , officer,untreated_crime = -1,0,0
for i in range(events):
    if crime == check[i]:
        if officer == 0:
            untreated_crime +=1
        else:
            officer += check[i]
    else:
        officer += check[i]
print(untreated_crime)
