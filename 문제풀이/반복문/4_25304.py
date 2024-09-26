a = int(input())
b = int(input())

for i in range(1,b+1):
    c,d=map(int,input().split())
    a = a-c*d

if a == 0:
    print("Yes")
else:
    print("No")