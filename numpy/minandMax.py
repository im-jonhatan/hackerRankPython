# Task
# You are given a 2-D array with dimensions NXM.
# Your task is to perform the min function over axis 1 and then find the max of that.

# Input Format
# The first line of input contains the space separated values of N and M.
# The next N lines contains M space separated integers.

# Output Format
# Compute the min along axis 1 and then print the max of that result.

# Sample Input
#     4 2
#     2 5
#     3 7
#     1 3
#     4 0

# Sample Output
#     3

# Explanation
# The min along axis 1 = [2, 3, 1, 0]
# The max of [2, 3, 1, 0] = 3
import numpy

n, m = map(int, input().split())
data = numpy.array([input().split() for _ in range(n)], int)

array_min = numpy.min(data, axis=1)
array_max = numpy.max(array_min)

print(array_max)
