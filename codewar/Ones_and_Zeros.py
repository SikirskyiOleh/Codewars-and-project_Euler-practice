# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

def binary_array_to_number(arr):
    # Best practice
    return int("".join(map(str, arr)), 2)
