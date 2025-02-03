n=int(input())
st=input()
nA=0
nD=0
for i in range(len(st)):
    if st[i]=="D":
        nD +=1
    else:
        nA +=1
if nD>nA:
    print("Danik")
elif nA==nD:
    print("Friendship")
else:
    print("Anton")
