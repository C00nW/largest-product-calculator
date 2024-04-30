from math import prod

def largest_product(series, length):
    # Check if the length is smaller than the series length
    if len(series) < length:
        return "ValueError: Length must be smaller than the series length."
    
    # Check if the length is negative
    if length < 0:
        return "ValueError: Length must not be negative."
    
    # Check if the series contains only digits
    if not series.isdigit():
        return "ValueError: Series must only contain digits."

    # Find the largest product 
    max_product = 0
    for i in range(len(series) - length + 1):
        substring = series[i:i+length]
        digits = [int(d) for d in substring]
        product = prod(digits)
        max_product = max(max_product, product)

    # Return the largest product
    return max_product

# Loop (repeat) until the user chooses to stop
while True:
    # Bonus Task: Getting input from the user through prompts
    series = input("Enter the series of digits: ")
    length = int(input("Enter the length of the series: "))

    # Calculate the largest product
    result = largest_product(series, length)
    
    # Print the result or error message
    if isinstance(result, str):
        print(result)
    else:
        print(f"The largest series product is: {result}")

    # Ask if the user wants to try again or exit the program
    repeat = input("Press 'y' to try again or any other key to exit program: ")
    if repeat.lower() != "y":
        break

# Say goodbye by thanking the user for using the program
print("Thank you for using the program!")