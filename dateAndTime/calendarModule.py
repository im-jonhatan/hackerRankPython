# You are given a date. Your task is to find what the day is on that date.

# Input Format
# A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

# Constraints
# • 2000 < year < 3000

# Output Format
# Output the correct day in capital letters.

# Sample Input
#     08 05 2015

# Sample Output
#     WEDNESDAY

# Explanation
# The day on August 5th 2015 was WEDNESDAY.

from calendar import weekday
from calendar import day_name

if __name__ == "__main__":
    date = list(map(int, input().split()))
    month = date[0]
    day = date[1]
    year = date[2]
    position_day = weekday(year, month, day)
    name_day = day_name[position_day]
    print(name_day.upper())
