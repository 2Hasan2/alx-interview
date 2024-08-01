#!/usr/bin/python3
"""A module for determining if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): A list of lists where each inner list
        contains keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.

    The function starts with the first box (index 0) which is unlocked by
    default. It uses a set to keep track of seen and unseen boxes. It
    performs a while loop to explore all boxes that can be unlocked using
    the keys found in each unlocked box. After processing, it checks if all
    boxes are unlocked by comparing the count of seen boxes to the total
    number of boxes.
    """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))

    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if boxIdx < 0 or boxIdx >= n:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)

    return n == len(seen_boxes)
