# a[0] = a[1] = 1
# a[2n] = A[n] + A[n-1]
# a[2n + 1] = A[n] - A[n-1]

data = [0] * 80
data[0] = 1
data[1] = 1

for i in range(2, 80):
    if i % 2 == 0:
        k = i // 2
        data[i] = data[k] + data[k - 1]
    else:
        k = (i - 1) // 2
        data[i] = data[k] - data[k - 1]

n = int(input())
print(data[n])

# for k in range(2, 41):
#     with open("tests/{num:03d}.dat".format(num=k), 'w') as dat, open("tests/{num:03d}.ans".format(num=k), 'w') as ans:
#         dat.write("{}\n".format(k - 1))
#         ans.write("{}\n".format(data[k - 1]))

# for k in range(2, 41):
#     with open("tests/{num:03d}.dat".format(num=k), 'w') as dat, open("tests/{num:03d}.ans".format(num=k), 'w') as ans:
