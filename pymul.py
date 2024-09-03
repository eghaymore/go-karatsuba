# This is to be used for timing purposes in comparison with the karatsuba implementations
import sys

def main():
    if ( len(sys.argv) != 3):
        print("Only accepting exactly two arguments")
        return
    # Print all command-line arguments
    print(int(sys.argv[1]) * int(sys.argv[2]))

if __name__ == "__main__":
    main()

