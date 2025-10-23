a,b,c=map(int,input().split())
while a!=0 and b!=0 and c!=0:
    if max(a,b,c)*2>=a+b+c:
        print("Invalid")
    elif a==b==c:
        print("Equilateral")
    elif a==b or a==c or b==c:
        print("Isosceles")
    else:
        print("Scalene")
    a,b,c=map(int,input().split())