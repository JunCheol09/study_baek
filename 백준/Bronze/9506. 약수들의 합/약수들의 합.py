a=int(input())
while a!=-1:
    x=0
    t=[]
    for i in range(1,a):
        if (a%i)==0:
            x+=i
            t.append(i)
    if x==a:
        for j in t:
            if j==1:
                print(f'{a} = 1 +',end="")
            elif j!=t[-1]:
                print(f' {j} +',end="")
            else:
                print(f' {j}')
        
    else:
        print(f'{a} is NOT perfect.')


    a=int(input())