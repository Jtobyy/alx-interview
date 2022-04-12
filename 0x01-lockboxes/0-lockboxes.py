#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    """
    boxes_length = len(boxes)
    for box in range(1, boxes_length):
        found = False
        counter = 0
        for temp_box in boxes:
            if counter != box:
                for key in temp_box:
                    if key == box:
                        found = True
                        break
                if found is True:
                    break
            counter += 1
        else:
            return False
    return True
