a,b = map(int,input().split())

if a >= 1 and b < 45:
    print(a-1,b + 15)
elif a >=1 and b >= 45:
    print(a,b-45)
elif a < 1 and b < 45:
    print(a + 23, b + 15)
else:
    print(0,b-45)