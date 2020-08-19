# Consider the following:

# A string, s, of length n where s = c0 c1 ... cn.
# An integer, k, where k is a factor of n.
# We can split s into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:
# - The characters in ui are a subsequence of the characters in ti.
# - Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index  j in t occurs at a previous index <j in ti, then do not include the character in string .
# Given  and , print  lines where each line  denotes string ui.

# Input Format
# The first line contains a single string denoting s.
# The second line contains an integer, k, denoting the length of each subsegment.

# Constraints
# 1 ≤ n ≤ 10ˆ4, where n is the length of s
# 1 ≤ k ≤ n
# It is guaranteed that n is a multiple of k.

# Output Format
# Print n/k lines where each line i contains string ui.

def merge_the_tools(string, k):
    for i in range(int(len(string) / k)):
        t = ''
        for c in string[i * k : (i + 1) * k]:
            if c not in t:
                t += c
        print(t)