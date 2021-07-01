# You are given a string S.
# contains alphanumeric characters only.
# Your task is to sort the string S in the following manner:
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

# Input Format
# A single line of input contains the string S.

# Constraints
# 0 < len(S) < 1000

# Output Format
# Output the sorted string S.

# Sample Input
#     Sorting1234

# Sample Output
#     ginortS1324

import re

S = "".join(sorted(input()))
l = re.findall('[a-z]', S)
u = re.findall('[A-Z]', S)
o = re.findall('[13579]', S)
e = re.findall('[24680]', S)
data = l + u + o + e
print("".join(data))
