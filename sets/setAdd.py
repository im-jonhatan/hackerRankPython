# Apply your knowledge of the .add() operation to help your friend Rupal.
# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.
# Find the total number of distinct country stamps.

# Input Format
# The first line contains an integer N, the total number of country stamps.
# The next N lines contains the name of the country where the stamp is from.

# Constraints
# 0 < N < 1000

# Output Format
# Output the total number of distinct country stamps on a single line.

if __name__ == "__main__":
    # define variables
    n = int(input())
    countries = set()
    # constraint 0 < n < 1000
    if n > 0 and n < 1000:
        # get countries
        for _ in range(n):
            country = input()
            # validate if country already exist
            if country not in countries:
                countries.add(country)
    
    print(len(countries))