# Perform append, pop, popleft and appendleft methods on an empty deque d.

# Input Format
# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods and their values.

# Constraints
# 0 < N ≤ 100

# Output Format
# Print the space separated elements of deque d.

# Sample Input
#     6
#     append 1
#     append 2
#     append 3
#     appendleft 4
#     pop
#     popleft

# Sample Output
#     1 2


from collections import deque

if __name__ == "__main__":
    d = deque()
    n = int(input())
    for _ in range(n):
        command = list(input().split())
        if command[0] == "pop":
            d.pop()
        elif command[0] == "popleft":
            d.popleft()
        elif command[0] == "append":
            d.append(command[1])
        elif command[0] == "appendleft":
            d.appendleft(command[1])

    print(" ".join(d))
