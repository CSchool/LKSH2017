# 0 < n < 100
#  0 < m < 10
# -100 < value < 100
# в одну строку

n = int(input())
answer = ''

for i in range(n):
    m = int(input())
    row = map(int, input().split())
    answer += "{} ".format(sum(1 for number in row if number < 0))

print(answer)
# import random
#
# for k in range(2, 21):
#     with open("tests/{num:03d}.dat".format(num=k), 'w') as dat, open("tests/{num:03d}.ans".format(num=k), 'w') as ans:
#         data = []
#         n = random.randint(1, 99)
#
#         dat.write("{}\n".format(n))
#         for i in range(0, n):
#             m = random.randint(1, 9)
#             dat.write("{}\n".format(m))
#
#             row = []
#             for j in range(0, m):
#                 row.append(random.randint(-100, 100))
#
#             dat.write(" ".join((str(x) for x in row)))
#             dat.write("\n")
#
#             ans.write("{} ".format(sum(1 for number in row if number < 0)))