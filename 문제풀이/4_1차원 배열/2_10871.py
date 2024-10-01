a,b = map(int,input().split())
for c in list(map(int,input().split())):
    if c < b:
        print(c,end=" ")
    else:
        continue

# 10 5
# 1 10 4 9 2 3 8 5 7 6