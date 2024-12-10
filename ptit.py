# Script to calculate the sum of even numbers from 1 to 100

# Initialize the sum variable
even_sum = 0

# Loop through numbers from 1 to 100
for num in range(1, 101):
    if num % 2 == 0:  # Check if the number is even
        even_sum += num  # Add it to the sum

# Print the result
print(f"The sum of even numbers from 1 to 100 is: {even_sum}")
