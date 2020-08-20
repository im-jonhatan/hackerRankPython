# In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.

# Constraints
# 1 ≤ n ≤ 10000
# 1 ≤ m ≤ 100
# 1 ≤ length of each word in the input ≤ 100

# Input Format
# The first line contains integers, n and m separated by a space.
# The next n lines contains the words belonging to group A.
# The next m lines contains the words belonging to group B.

# Output Format
# Output m lines.
# The iˆth line should contain the 1-indexed positions of the occurrences of the iˆth word separated by spaces.

# Sample Input
#     5 2
#     a
#     a
#     b
#     a
#     b
#     a
#     b

# Sample Output
#     1 2 4
#     3 5

# Explanation
# 'a' appeared 3 times in positions 1, 2 and 4.
# 'b' appeared 2 times in positions 3 and 5.
# In the sample problem, if 'c' also appeared in word group B, you would print -1.

from collections import defaultdict


if __name__ == "__main__":
    n, m = map(int, input().split())
    words = {}
    for i in range(n):
        s = input()
        if s not in words:
            words[s] = [i+1]
        else:
            words[s].append(i+1)
    
    for _ in range(m):
        s = input()
        if s in words:
            print(" ".join(map(str, words[s])))
        else:
            print("-1")