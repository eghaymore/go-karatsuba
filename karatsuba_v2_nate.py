# KARATSUBA MULTIPLICATION V2
# Nathan Hanzel
# Note on implementation: For this version I am padding the numbers as they are iterated over in the recursive function
# to see which approach is faster.
# Also, all numbers are treated as strings until very end to make left padding easier

import time
from helper import *

def karatsuba(x, y):
    x,y = recursive_length_format(x,y)
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

start_time = time.perf_counter()
# Preconditioning data
max_len = max(len(x), len(y))

x = x.zfill(max_len)
y = y.zfill(max_len)

print("x: " + x)
print("y: " + y)

result = karatsuba(x,y)
end_time = time.perf_counter()
print("V2 Result: " + result + " Time: " + str(end_time - start_time))