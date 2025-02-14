#!/usr/bin/env python3
# Author ID: nkayer

def add(number1, number2):
    try:
        # Try to convert both numbers to float and return the sum
        return float(number1) + float(number2)
    except ValueError:
        # If there's a ValueError, return the error message
        return 'error: could not add numbers'

def read_file(filename):
    try:
        # Try to open the file in read mode
        with open(filename, 'r') as file:
            # Read all lines from the file
            return file.readlines()
    except (FileNotFoundError, IOError):
        # If there's an error (file not found or other I/O error), return the error message
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))  # works
    print(add('10', 5))  # works
    print(add('abc', 5))  # exception
    print(read_file('seneca2.txt'))  # works
    print(read_file('file10000.txt'))  # exception

