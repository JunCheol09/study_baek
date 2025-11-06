a=int(input())
b=list(map(int,input().split()))
c=int(input())


for i in range(a):
    b.append(c-b[i])

len_num=2*a-len(list(set(b)))



if c/2 in b:
    len_num-=1
        



print(len_num//2)