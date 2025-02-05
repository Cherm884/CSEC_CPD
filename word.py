s=input()
n=len(s)//2
res=0
for i in range(len(s)):
    if s[i].isupper():
        res +=1
if res>n:
    a=s.upper()
else:
    a=s.lower()
print(a)
