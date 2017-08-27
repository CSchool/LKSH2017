import sys
n, s = map(int, input().split())

q = list(map(int, input().split()))

for b in range(1 << n):
    e = 0
    t = ""
    for i in range(n):
        if (b >> i) & 1:
            e += q[i]
            if i == 0:
                t += str(q[i])
            else:
                t += " + " + str(q[i])
        else:
            e -= q[i]
            if i == 0:
                t += "-" + str(q[i])
            else:
                t += " - " + str(q[i])
    if e == s:
        print(t, "=", s)
        sys.exit(0)
print("No solution")