a=int(input())
b=[]
c=0
for i in range(a):
    x,y=input().split()
    if c==1:
        if x in b or y in b:
            b.append(x)
            b.append(y)

    elif x=="ChongChong" or y=="ChongChong":
        b.append(x)
        b.append(y)
        c=1
print(len(list(set(b))))
