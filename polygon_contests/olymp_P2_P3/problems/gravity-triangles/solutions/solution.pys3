from math import hypot

n = int(input())

p = []
for _ in range(n):
    p.append(tuple(map(float, input().split())))

qi, qj, qk = 0, 0, 0
q = -1

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or i == k or j == k:
                continue
            pp = hypot(p[i][0] - p[j][0], p[i][1] - p[j][1]) + hypot(p[k][0] - p[j][0], p[k][1] - p[j][1]) + hypot(p[i][0] - p[k][0], p[i][1] - p[k][1])
            if pp > q:
                qi, qj, qk = i, j, k
                q = pp

print(' '.join(map(str, p[qi])))
print(' '.join(map(str, p[qj])))
print(' '.join(map(str, p[qk])))