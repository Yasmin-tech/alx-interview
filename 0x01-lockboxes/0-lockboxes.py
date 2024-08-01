#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def join(T, R):
    res = []
    for e in R:
        res += T[e]
        return res


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    index = 0
    total = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in join(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                added = True
    return len(total) == len(boxes)
