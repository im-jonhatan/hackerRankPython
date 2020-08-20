# You are given a complex z. Your task is to convert it to polar coordinates.

# Input Format
# A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a complex number.

# Constraints
# Given number is a valid complex number

# Output Format
# Output two lines:
# The first line should contain the value of ρ.
# The second line should contain the value of φ.

from cmath import phase

if __name__ == "__main__":
    n_complex = input()
    n_abs = abs(complex(n_complex))
    n_phase = phase(complex(n_complex))
    print("{}".format(n_abs))
    print("{}".format(n_phase))