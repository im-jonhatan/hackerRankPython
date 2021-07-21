# Task
# You are given a NXM integer array matrix with space separated elements (N=rows and M=columns).
# Your task is to print the transpose and flatten results.

# Input Format
# The first line contains the space separated values of N and M.
# The next N lines contains the space separated elements of M columns.

# Output Format
# First, print the transpose array and then print the flatten.

# Sample Input
#     2 2
#     1 2
#     3 4

# Sample Output
#     [[1 3]
#     [2 4]]
#     [1 2 3 4]
import numpy


n, m = input().split()
data = []

for _ in range(int(n)):
    arr = input().strip().split(' ')
    data.append(arr)

my_array = numpy.array(data, int)

print(numpy.transpose(my_array))
print(my_array.flatten())
