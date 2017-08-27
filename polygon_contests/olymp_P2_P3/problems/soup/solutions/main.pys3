dimensions = ()

data = []
allowed_data = {666, 4, 13}
isAllowedArray = True

n, m = map(int, input().split())

for i in range(0, n):
    data.append(list(map(int, input().split())))


for i in range(0, n):
    for j in range(0, m):
        if data[i][j] not in allowed_data:
            print("NO")
            exit(0)

print("YES")