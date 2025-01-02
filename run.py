import sys

# Define the character set including lowercase, uppercase, and digits
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Function to calculate the decimal value of a base-62 string
def base62_to_decimal(number_plate, charset):
    base = len(charset)
    decimal_value = 0
    for char in number_plate:
        decimal_value = decimal_value * base + charset.index(char)
    return decimal_value

# Check if two arguments are passed
if len(sys.argv) != 3:
    print("Usage: python script.py <firstNumberPlate> <secondNumberPlate>")
    sys.exit(1)

# Take input from the command line
firstNumberPlate = sys.argv[1]
secondNumberPlate = sys.argv[2]

# Calculate the decimal values for each number plate
decimal_firstNumberPlate = base62_to_decimal(firstNumberPlate, charset)
decimal_secondNumberPlate = base62_to_decimal(secondNumberPlate, charset)

# Calculate the number of plates generated between them
plates_between = abs(decimal_secondNumberPlate - decimal_firstNumberPlate)

print(f"Number of plates generated between {firstNumberPlate} and {secondNumberPlate}: {plates_between}")