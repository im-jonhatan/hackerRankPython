# You are given three integers: a, b, and m, respectively. Print two lines.
# The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).

# Input Format
# The first line contains a, the second line contains b, and the third line contains m.

# Constraints
# 1 ≤ a ≤ 10
# 1 ≤ b ≤ 10
# 2 ≤ m ≤ 1000

# Sample Input
#     3
#     4
#     5

# Sample Output
#     81
#     1

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = int(input())
    print("{:d}".format(pow(a, b)))
    print("{:d}".format(pow(a, b, m)))