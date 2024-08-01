#!/usr/bin/python3
'''A module for determining if all boxes can be unlocked.
'''


def canUnlockAll(boxes):
    '''Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): A list of lists where each inner list contains keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.

    The function starts with the first box (index 0) which is unlocked by default. It uses Breadth-First Search (BFS)
    to explore all the boxes that can be unlocked using the keys found in each unlocked box. It tracks the unlocked 
    boxes in a set and uses a queue to manage the boxes to be processed. After processing, it checks if all boxes are 
    unlocked by comparing the count of unlocked boxes to the total number of boxes.
    '''
    unlocked = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        if current_box not in unlocked:
            unlocked.add(current_box)
            # Add all boxes that can be unlocked by the current box's keys
            for key in boxes[current_box]:
                if key < len(boxes) and key not in unlocked:
                    queue.append(key)

    # Check if all boxes are unlocked
    return len(unlocked) == len(boxes)
