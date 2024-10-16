# Pattern
def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")  # Print the number 'i' i times
        print()  # Move to the next line after each row

# Input from the user
n = int(input("Enter the value of n: "))

# Print the pattern
print_pattern(n)