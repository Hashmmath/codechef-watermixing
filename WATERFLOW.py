n = int(input())
for i in range(n):
    a,b,c,d = [int(x) for x in input().split()]
    m = c*d
    s = a+m
    if(s==b):
        print("filled")
    elif(s>b):
        print("overflow")
    else:
        print("Unfilled")