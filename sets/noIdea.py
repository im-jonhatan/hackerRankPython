# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i ∈ A, you add 1 to your happiness. If i ∈ B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
# Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

# Constraints
# 1 ≤ n ≤ 10ˆ5
# 1 ≤ m ≤ 10ˆ5
# 1 ≤ any integer in the input ≤ 10ˆ9

# Input Format

# The first line contains integers  and  separated by a space.
# The second line contains  integers, the elements of the array.
# The third and fourth lines contain  integers,  and , respectively.

# Output Format
# Output a single integer, your total happiness.


if __name__ == "__main__":
    n, m = (int(i) for i in input().split())
    l = map(int, input().strip().split(' '))
    a = set(map(int, input().strip().split(' ')))
    b = set(map(int, input().strip().split(' ')))
    result = 0
    for i in l:
        if i in a:
            result += 1
        if i in b:
            result += -1
    print(result)