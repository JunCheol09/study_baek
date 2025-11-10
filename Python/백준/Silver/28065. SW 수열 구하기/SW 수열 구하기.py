a=int(input())
k=a
b = [i for i in range(1, a)]

x=a
for i in range(k):
    if i==k-1:
        print(a)
    elif i%2==0:
        
        print(a,end=" ")
        x+=-1
        a+=-x
    else:
        print(a,end=" ")
        x+=-1
        a+=x