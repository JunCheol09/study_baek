a=int(input())
b=input()
t=[]
c=0
for i in range(a-1):
    x=input()
    if x!="ENTER":
        t.append(x)
    else:
        new_name=set(t)
        c+=len(new_name)
        t=[]
        
new_name=set(t)
c+=len(new_name)
print(c)