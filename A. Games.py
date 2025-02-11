from collections import defaultdict
 
n =int(input())
count_h =defaultdict(int)
count_g= defaultdict(int)
 
for i in range(n):
    h , g = map(int,input().split())
    count_h[h] +=1
    count_g[g] +=1
res =0
 
for key, val in count_h.items():
    res =res +(val * count_g[key])
 
print(res)
