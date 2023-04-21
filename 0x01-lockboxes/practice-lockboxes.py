#!/usr/bin/env python3

"""Script that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    keys = [0]

    for key in keys:
        for key in boxes[key]:
            if key not in keys and key < len(boxes):
                keys.append(key)
    if len(keys) == len(boxes):
        return True
    return False