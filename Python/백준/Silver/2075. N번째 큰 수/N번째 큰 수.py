a=int(input())
d=[]
for i in range(a):
    c=list(map(int,input().split()))
    for j in c:
        d.append(j)
    d.sort(reverse=True)
    d=d[0:a]
print(d[a-1])

