a,b = map(int,input().split())
c = int(input())
d = c//60
e = c%60
if b + e >= 60:
    if a + d + 1 >= 24:
        print(a + d - 23,b+e-60)
    else:
        print(a + d + 1,b+e-60)
else:
    if a + d >= 24:
        print(a + d - 24,b+e)
    else:
        print(a + d,b+e)