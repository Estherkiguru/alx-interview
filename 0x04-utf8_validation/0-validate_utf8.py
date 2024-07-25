#!/usr/bin/python3
"""
0-UTF-8 Validation
"""


def validUTF8(data):
    """
    method that determines if data set repr a valid UTF-8 encoding.
    Return: True if data is a valid UTF-8
    encoding, else return False
    """
    num_byte = 0

    for byte in data:
        if num_byte == 0:
            if byte >> 5 == 0b110 or byte >> 5 == 0b1110:
                num_byte = 1
            elif byte >> 4 == 0b1110:
                num_byte = 2
            elif byte >> 3 == 0b11110:
                num_byte = 3
            elif byte >> 7 == 0b1:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_byte -= 1
    return num_byte == 0
