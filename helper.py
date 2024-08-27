#
# HELPER FUNCTIONS
#

# Split string-int in half
def split_string_number(n):
    num_digits = len(n)
    midpoint = num_digits // 2
    
    first_half, second_half = n[:midpoint], n[midpoint:]
    
    return first_half, second_half

# Find the next highest power of 2
def next_power_of_2(n):
    return 1 << (n - 1).bit_length()

# Format data for karatsuba function
def precondition(x,y):
    max_len = max(len(x), len(y))
    new_length = next_power_of_2(max_len)

    padded_x = x.zfill(new_length)
    padded_y = y.zfill(new_length)

    return padded_x, padded_y