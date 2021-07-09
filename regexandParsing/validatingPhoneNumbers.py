# Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
# A valid mobile number is a ten digit number starting with a 7, 8 or 9.

# Input Format
# The first line contains an integer N, the number of inputs.
# N lines follow, each containing some string.

# Constraints
# 1 ≤  N ≤  10
# 2 ≤  len(Numbers) ≤ 15

# Output Format
# For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

# Sample Input
#     2
#     9587456281
#     1252478965

# Sample Output
#     YES
#     NO

import re

N = int(input())
for _ in range(N):
    phone = input()
    if re.match(r'^[789]\d{9}$', phone):
        print('YES')
    else:
        print('NO')
