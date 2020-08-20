# You are given a string S.
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

# Input Format
# A single line containing the space separated string S and the integer value k.

# Constraints
# 0 < k ≤ len(S)
# The string contains only UPPERCASE characters.

# Output Format
# Print the permutations of the string  on separate lines.

# Sample Input
# HACK 2

# Sample Output
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH

# Explanation
# All possible size  permutations of the string "HACK" are printed in lexicographic sorted order.

from itertools import permutations

if __name__ == "__main__":
    S, k = map(str, input().split())
    S = sorted(list(map(str, S)))
    k = int(k)
    result = list(permutations(S, k))
    for item in result:
        print("".join(item))