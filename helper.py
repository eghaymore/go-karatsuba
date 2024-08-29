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

def fix_lengths(x,y):
    length = max(len(x), len(y))
    if (length < 4 and len(x) != len(y)):
        x = x.zfill(next_power_of_2(length))
        y = y.zfill(next_power_of_2(length))
    return x,y

# Format data for karatsuba function
def precondition(x,y):
    max_len = max(len(x), len(y))
    new_length = next_power_of_2(max_len)

    padded_x = x.zfill(new_length)
    padded_y = y.zfill(new_length)

    return padded_x, padded_y

def mult_lookup_table(n):
    times_table = { "00": "0", "01": "0", "02": "0", "03": "0", "04": "0", "05": "0", "06": "0", "07": "0", "08": "0", "09": "0",
                    "10": "0", "11": "1", "12": "2", "13": "3", "14": "4", "15": "5", "16": "6", "17": "7", "18": "8", "19": "9",
                    "20": "0", "21": "2", "22": "4", "23": "6", "24": "8", "25": "10", "26": "12", "27": "14", "28": "16", "29": "18",
                    "30": "0", "31": "3", "32": "6", "33": "9", "34": "12", "35": "15", "36": "18", "37": "21", "38": "24", "39": "27",
                    "40": "0", "41": "4", "42": "8", "43": "12", "44": "16", "45": "20", "46": "24", "47": "28", "48": "32", "49": "36",
                    "50": "0", "51": "5", "52": "10", "53": "15", "54": "20", "55": "25", "56": "30", "57": "35", "58": "40", "59": "45",
                    "60": "0", "61": "6", "62": "12", "63": "18", "64": "24", "65": "30", "66": "36", "67": "42", "68": "48", "69": "54",
                    "70": "0", "71": "7", "72": "14", "73": "21", "74": "28", "75": "35", "76": "42", "77": "49", "78": "56", "79": "63",
                    "80": "0", "81": "8", "82": "16", "83": "24", "84": "32", "85": "40", "86": "48", "87": "56", "88": "64", "89": "72",
                    "90": "0", "91": "9", "92": "18", "93": "27", "94": "36", "95": "45", "96": "54", "97": "63", "98": "72", "99": "81"}
    return times_table[n]