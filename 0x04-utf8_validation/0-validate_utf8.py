#!/usr/bin/python3
"""
method that determines if a given data set represents a valid UTF-8 encoding.
"""

from typing import List


def validUTF8(data):
    """ Determining a given data is valid UTF """
    count = 0
    index = 0

    while count < len(data):
        index = data[count]

        # Using bit shifting to extract relevant bits from each byte
        # Checking how many bytes there are in the current character
        # Checking if bytes are leading or continuation bytes
        if index >> 5 == 0b110:
            count += 1
        elif index >> 4 == 0b1110:
            count += 2
        elif index >> 3 == 0b11110:
            count += 3
        elif index >> 7 == 0:
            count += 1
        else:
            return False

    return True
