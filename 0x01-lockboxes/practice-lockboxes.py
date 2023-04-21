#!/usr/bin/env python3

"""Script that determines if all the boxes can be opened"""


def canUnlockAll(boxes):    # takes a list of lists boxes as its input
    keys = [0]  # list of keys containing the key to the first box 

    for key in keys:    # Looping through the keys list
        for key in boxes[key]:
            # We use a loop to go through each key in the keys list:
            # For each key, we go through the box at that key in the boxes list.
            # For each key we find in that box (i.e., a new key), we check if it is not already in the keys list and that it is a valid index (i.e., less than the length of the boxes list).
            # If the new key satisfies these conditions, we add it to the keys list.
            if key not in keys and key < len(boxes):
                keys.append(key)
    if len(keys) == len(boxes):
        return True
    return False