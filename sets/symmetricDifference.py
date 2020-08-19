# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Input Format
# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.

# Output Format
# Output the symmetric difference integers in ascending order, one per line.

if __name__ == "__main__":
    n = int(input())
    n_values = set(map(int, input().split()))
    m = int(input())
    m_values = set(map(int, input().split()))

    result = (n_values.difference(m_values)).union(m_values.difference(n_values))
    for item in sorted(result):
        print("{}".format(item))