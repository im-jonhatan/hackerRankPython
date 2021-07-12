# ABCXYZ company has up to 100 employees.
# The company decides to create a unique identification number(UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.
# A valid UID must follow the rules below:
# - It must contain at least  uppercase English alphabet characters.
# - It must contain at least  digits(-).
# - It should only contain alphanumeric characters(a-z, A-Z & 0-9).
# - No character should repeat.
# There must be exactly 10 characters in a valid UID.

# Input Format
# The first line contains an integer T, the number of test cases.
# The next T lines contains an employee's UID.

# Output Format
# For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

# Sample Input
#     2
#     B1CD102354
#     B1CDEF2354

# Sample Output
#     Invalid
#     Valid

# Explanation
# B1CD102354: 1 is repeating → Invalid
# B1CDEF2354: Valid

import re 

def validate(uuid):
    """ validate:
        at least 2 uppercase.
        at least 3 numbers.
        should have 10 values.
        every character must be unique.
    """
    if len(re.findall(r'[A-Z]', uuid)) < 2:
        return 'Invalid'
    elif len(re.findall(r'\d', uuid)) < 3:
        return 'Invalid'
    elif len(re.findall(r'[a-zA-Z\d]', uuid)) != 10:
        return 'Invalid'
    elif re.findall(r'.*(.).*\1', uuid):
        return 'Invalid'
    return 'Valid'


T = int(input())

for _ in range(T):
    uuid = input()
    print(validate(uuid))
