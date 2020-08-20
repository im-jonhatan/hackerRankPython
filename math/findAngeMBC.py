# ABC is a right triangle, 90º at B.
# Therefore, ABC = 90º
# Point M is the midpoint of hypotenuse AC.

# You are given the lengths AB and BC.
# Your task is to find MBC (angle Øº, as shown in the figure) in degrees.

# Input Format

# The first line contains the length of side AB.
# The second line contains the length of side BC.

# Constraints
# 0 < AB ≤ 100
# 0 < BC ≤ 100
# Lengths AB and BC are natural numbers.

# Output Format
# Output MBC in degrees.
# Note: Round the angle to the nearest integer.


import math
if __name__ == "__main__":
    import math
    AB = float(input())
    BC = float(input())

    print(str(int(round(math.degrees(math.atan2(AB, BC)))))+'°')