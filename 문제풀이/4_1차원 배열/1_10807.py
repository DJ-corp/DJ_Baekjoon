a = int(input())
b = list(map(int,input().split()))
v = int(input())
count = 0
for c in b:
    if c == v:
        count += 1
    else:
        continue
print(count)

# 11
# 1 4 1 2 4 2 4 2 3 4 4
# 2