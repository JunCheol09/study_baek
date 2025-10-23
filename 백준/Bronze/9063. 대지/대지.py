a=int(input())
xr=[]
yr=[]
for i in range(a):
    x,y=map(int,input().split())
    xr.append(x)
    yr.append(y)
if a==1:
    print(0)
else:
    print((max(xr)-min(xr))*(max(yr)-min(yr)))
    
    
        
    