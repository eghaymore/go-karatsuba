# Karatsuba's algorithm
# Sam Collins
# All multiplication is placed in logs
# Requires inputs to multiply

# Function to make the two integers the same length for recursion by adding zeros.
def zeroPad(numberString, zeros, padLeft=True):
    """Return the string with zeros added to the left or right."""
    if padLeft:
        return '0' * zeros + numberString
    else:
        return numberString + '0' * zeros

def karatsubaMultiplication(num1, num2, depth=0):
    """Multiply two integers using Karatsuba's algorithm with detailed logging."""
    indent = '    ' * depth  # Indentation for better readability in logs
    print(f"{indent}Multiplying {num1} and {num2}")
    
    # Convert numbers to strings for easy digit access
    num1_str = str(num1)
    num2_str = str(num2)
    
    # Base case for recursion: single-digit multiplication
    if len(num1_str) == 1 and len(num2_str) == 1:
        result = int(num1_str) * int(num2_str)
        print(f"{indent}Base case: {num1_str} * {num2_str} = {result}")
        return result
    
    # Make the lengths of num1 and num2 equal by padding with zeros
    if len(num1_str) < len(num2_str):
        num1_str = zeroPad(num1_str, len(num2_str) - len(num1_str))
    elif len(num2_str) < len(num1_str):
        num2_str = zeroPad(num2_str, len(num1_str) - len(num2_str))
    
    n = len(num1_str)
    mid = n // 2
    
    # Split num1 and num2 into upper (left) and lower (right) parts
    upper1 = int(num1_str[:mid])  # First half of num1
    lower1 = int(num1_str[mid:])  # Second half of num1
    upper2 = int(num2_str[:mid])  # First half of num2
    lower2 = int(num2_str[mid:])  # Second half of num2
    
    print(f"{indent}Split {num1_str} into {upper1} and {lower1}")
    print(f"{indent}Split {num2_str} into {upper2} and {lower2}")
    
    # Recursively calculate the three required products
    product_upper = karatsubaMultiplication(upper1, upper2, depth + 1)  # (upper1 * upper2)
    product_lower = karatsubaMultiplication(lower1, lower2, depth + 1)  # (lower1 * lower2)
    product_cross = karatsubaMultiplication(upper1 + lower1, upper2 + lower2, depth + 1)
    
    # Calculate the final result using Karatsuba's formula
    product_A = int(zeroPad(str(product_upper), 2 * (n - mid), False))
    product_B = int(zeroPad(str(product_cross - product_upper - product_lower), n - mid, False))
    
    result = product_A + product_B + product_lower
    print(f"{indent}product_upper = {product_upper}, product_lower = {product_lower}, (upper1+lower1)*(upper2+lower2) = {product_cross}")
    print(f"{indent}product_A = {product_A}, product_B = {product_B}")
    print(f"{indent}Result = {product_A} + {product_B} + {product_lower} = {result}")
    
    return result

def get_user_input():
    """Get valid user input for Karatsuba multiplication."""
    while True:
        try:
            num1 = int(input("Enter the first positive integer: "))
            num2 = int(input("Enter the second positive integer: "))
            
            if num1 < 0 or num2 < 0:
                raise ValueError("Inputs must be non-negative integers.")
            
            return num1, num2
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main():
    print("Karatsuba Multiplication")
    num1, num2 = get_user_input()
    
    print("\nStarting Karatsuba Multiplication...\n")
    result = karatsubaMultiplication(num1, num2)
    
    print(f"\nFinal Result: {num1} * {num2} = {result}")

if __name__ == "__main__":
    main()
