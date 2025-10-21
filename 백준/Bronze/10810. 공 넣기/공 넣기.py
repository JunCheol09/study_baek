a,b= map(int,input().split())
x=[]

for i in range(a):
    x.append(0)



for l in range(b):
    a=[]
    i,j,k=map(int,input().split())
    for h in range(i-1,j):
      x[h]=k
print(*x)
    
    
  


