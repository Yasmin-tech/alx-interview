#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    opened = set()

    if not boxes:
        return False
    if not boxes[0] and len(boxes) > 1:
        return False
    else:
        return True

    queue = [0]

    while queue:
        box = queue.pop(0)
        if box not in opened:
            opened.add(box)
            for key in boxes[box]:
                if key < len(boxes) and key not in opened:
                    queue.append(key)

    return len(opened) == len(boxes)
