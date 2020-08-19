# Task
# Now, let's use our knowledge of sets and help Mickey.
# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

# Formula used:
# average = sum of distinct heights / total number of distinct heights

# Input Format
# The first line contains the integer,N , the total number of plants.
# The second line contains the N space separated heights of the plants.

# Constraints
# 0 < N ≤ 100

# Output Format
# Output the average height value on a single line.


def average(array):
    total = 0
    for item in set(array):
        total += item
    total = total / len(set(array))
    return total