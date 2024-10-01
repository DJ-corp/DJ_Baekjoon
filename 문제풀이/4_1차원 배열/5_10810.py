a,b = map(int, input().split())
c = []
for i in range(a):
    c.append("")
for i in range(b):
    d,j,k = map(int,input().split())
    for e in range(d,j+1):
        c[e-1] = k
for i in c:
    if i != "":
        print(i,end = " ")
    else:
        print(0,end = " ")
# 5 4
# 1 2 3
# 3 4 4
# 1 4 1
# 2 2 2