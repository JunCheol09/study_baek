a=int(input())
from math import factorial
for i in range(a):
    c,d=map(int,input().split())
    x=factorial(d)
    y=factorial(c)
    z=factorial(d-c)
    print(x//(y*z))