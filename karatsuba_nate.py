# KARATSUBA MULTIPLICATION
# Nathan Hanzel
# Note on implementation: I am preconditioning both inputs (x and y) to be the same length
# and to be a power of 2. This is done outside of the actual karatsuba function to keep it clean :)
# Also, all numbers are treated as strings until very end to make left padding easier

from helper import *

def karatsuba(x, y):
    x,y = fix_lengths(x,y)
    print("x: " + x + " y: " + y)
    n = len(x)
    if (n == 1): # 1 digit is our base case (a, b, c, and d will always have the same number of digits)
        return mult_lookup_table(x + y)
    else:
        a , b = split_string_number(x)
        c, d = split_string_number(y)
        ac = int(karatsuba(a, c))
        bd = int(karatsuba(b, d))
        ad_bc = int(karatsuba(str(int(a)+int(b)), str(int(c)+int(d)))) - ac - bd
        return str((ac * 10 ** n) + bd + (ad_bc * 10 ** (n // 2)))

x = input("Enter first number: ")
y = input("Enter second number: ")

#x = 1234
#y = 5678

# Preconditioning data
x,y = precondition(x,y)
print("x: " + x)
print("y: " + y)

print(karatsuba(x,y))