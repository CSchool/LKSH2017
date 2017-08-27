#!/usr/bin/python3

import os
import math
import sys

test_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests')
i = 0


def solve(data):
    max_value = -math.inf
    answer = ()

    for i in range(0, len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                d1 = math.hypot(data[i][0] - data[j][0], data[i][1] - data[j][1])
                d2 = math.hypot(data[j][0] - data[k][0], data[j][1] - data[k][1])
                d3 = math.hypot(data[i][0] - data[k][0], data[i][1] - data[k][1])

                if d1 + d2 + d3 > max_value:
                    answer = [data[i], data[j], data[k]]
                    max_value = d1 + d2 + d3

    return answer

points = {
    'data': [],
    'count': 0
}

with open(sys.argv[1], 'r') as input_file:
    try:
        points['count'] = int(input_file.readline())
        raw_data = input_file.readlines()

        for line in raw_data:
            points['data'].append(tuple(map(float, line.split())))
    except Exception as e:
        print(str(e), file=sys.stderr)
        exit(1)

answer = solve(points['data'])
output_answer = ()

with open(sys.argv[2], 'r') as output_file:
    output_data = []
    try:
        for i in range(0, 3):
            out = output_file.readline().strip().split()
            output_data.append(tuple(map(float, out)))
    except Exception as e:
        print(str(e), file=sys.stderr)
        exit(1)

answer = sorted(answer)
output_data = sorted(output_data)

for i in range(0, len(answer)):
    if not (math.isclose(answer[i][0], output_data[i][0], rel_tol=1e-04) and math.isclose(answer[i][1], output_data[i][1], rel_tol=1e-04)):
        print("{} is not equal {}\n".format(str(output_data), str(answer)), file=sys.stderr)
        exit(1)

exit(0)

#if sorted(answer) == sorted(output_data):
#    exit(0)
#else:
#    print("{} is not equal {}\n".format(str(output_data), str(answer)), file=sys.stderr)
#    exit(5)

# point_count = 3
#
# for k in range(0, 5):
#     points = []
#     for p in range(0, point_count):
#         points.append((random.randint(-50, 50), random.randint(-50, 50)))
#
#     test_number = "{num:03d}".format(num=i)
#
#     with open(os.path.join(test_path, "{}.dat".format(test_number)), 'w') as input_file:
#         input_file.write("{}\n".format(point_count))
#         for point in points:
#             input_file.write("{} {}\n".format(*point))
#
#     with open(os.path.join(test_path, "{}.ans".format(test_number)), 'w') as output_file:
#         output_file.write("{} {} {}".format(*solve(points)))
#
#     point_count += 1
#     i += 1
#
# for k in range(0, 5):
#     points = []
#     for p in range(0, point_count):
#         points.append((random.uniform(-1000, 1000), random.uniform(-1000, 1000)))
#
#     test_number = "{num:03d}".format(num=i)
#
#     with open(os.path.join(test_path, "{}.dat".format(test_number)), 'w') as input_file:
#         input_file.write("{}\n".format(point_count))
#         for point in points:
#             input_file.write("{} {}\n".format(*point))
#
#     with open(os.path.join(test_path, "{}.ans".format(test_number)), 'w') as output_file:
#         output_file.write("{} {} {}".format(*solve(points)))
#
#     point_count += 1
#     i += 1
#
# point_count = 100
#
# points = []
# for p in range(0, point_count):
#     points.append((random.uniform(-1000, 1000), random.uniform(-1000, 1000)))
#
# test_number = "{num:03d}".format(num=i)
#
# with open(os.path.join(test_path, "{}.dat".format(test_number)), 'w') as input_file:
#     input_file.write("{}\n".format(point_count))
#     for point in points:
#         input_file.write("{} {}\n".format(*point))
#
# with open(os.path.join(test_path, "{}.ans".format(test_number)), 'w') as output_file:
#     output_file.write("{} {} {}".format(*solve(points)))
#
# point_count += 1
# i += 1