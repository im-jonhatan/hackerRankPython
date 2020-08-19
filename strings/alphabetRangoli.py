# You are given an integer, N. Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)
# The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

# Input Format
# Only one line of input containing N, the size of the rangoli.

# Constraints
# 0 < N < 27

# Output Format
# Print the alphabet rangoli in the format explained above.

import string


def print_rangoli(size):
    alphabet = string.ascii_lowercase[:size]
    height = (size * 2) - 1
    width = (size * 4) - 3
    lines = [None] * height
    for i in range(size):
        sub_alphabet = alphabet[(-i - 1):]
        letters = ''.join(reversed(sub_alphabet)) + sub_alphabet[1:]
        lines[i] = lines[-i - 1] = '-'.join(letters).center(width, '-')
    
    print(*lines, sep='\n')