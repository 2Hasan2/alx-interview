def canUnlockAll(boxes):
    # Initialize a set to track unlocked boxes
    unlocked = set()
    # Use a list as a queue for BFS
    queue = [0]

    # Perform BFS
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
