a=int(input())
b= list(map(int, input().split()))

x=[0]*a

for i in range(a):
    for j in range(i+1,a,1):
        if b[i]<=b[j]:
            x[j]=x[j]+1
        else:
            x[i]=x[i]+1

print(*x)
