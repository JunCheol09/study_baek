a,b= map(int,input().split())
x=[]

for i in range(a):
    x.append(i+1)



for l in range(b):
    
    i,j=map(int,input().split())
    x1=x[i-1]
    x2=x[j-1]
    x[i-1]=x2
    x[j-1]=x1
print(*x)
    
    
  


