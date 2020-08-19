# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2

# Input Format
# A single line containing a string S.

# Constraints
# 0 < len(S) ≤ 1000

# Output Format
# Print the modified string .

def swap_case(s):
    s_final = ""
    for letter in range(len(s)):
        if s[letter].isupper():
            s_final += s[letter].lower()
        else:
            s_final += s[letter].upper()
    return s_final