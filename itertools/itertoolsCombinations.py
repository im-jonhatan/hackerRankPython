# You are given a string S.
# Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

# Input Format
# A single line containing the string S and integer value k separated by a space.

# Constraints
# 0 < k ≤ len(S)
# The string contains only UPPERCASE characters.

# Output Format
# Print the different combinations of string  on separate lines.

# Sample Input
#     HACK 2

# Sample Output
#     A
#     C
#     H
#     K
#     AC
#     AH
#     AK
#     CH
#     CK
#     HK

from itertools import combinations

if __name__ == "__main__":
    string, groups = input().split()
    string = list(string)
    string.sort()
    groups = int(groups)
    result = list()
    for i in range(1, groups + 1):
        result += list(combinations(string, i))
    for item in result:
        print("".join(item))