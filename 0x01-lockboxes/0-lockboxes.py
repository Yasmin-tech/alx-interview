#!/usr/bin/python3
''' Solve the Lockboxes problem
    '''


from collections import deque


def canUnlockAll(boxes):
    ''' The Entery function that will be called with a list of lists
        '''
    number_of_boxes = len(boxes)

    queue_of_key = deque()
    set_of_opened_boxes = set()

    # The first box boxes[0] is unlocked
    set_of_opened_boxes.add(0)

    for key in boxes[0]:
        queue_of_key.append(key)

    # next_box = queue_of_key.popleft()
    # print(queue_of_key)
    # print(set_of_opened_boxes)
    result = openBoxes(queue_of_key, set_of_opened_boxes,
                       boxes, number_of_boxes)
    return result


def openBoxes(queue_of_key, set_of_opened_boxes, boxes, number_of_boxes):
    ''' This is a recursive function that keeps trying to open the boxes
        '''
    # print(queue_of_key)
    # print(set_of_opened_boxes)

    if (len(set_of_opened_boxes) == number_of_boxes):
        return True
    elif (not queue_of_key):
        return False
    else:
        current_box = queue_of_key.popleft()
        while (current_box in set_of_opened_boxes and queue_of_key):
            current_box = queue_of_key.popleft()
        if (not queue_of_key):
            return False
        set_of_opened_boxes.add(current_box)
        for key in boxes[current_box]:
            queue_of_key.append(key)

        return openBoxes(queue_of_key, set_of_opened_boxes,
                         boxes, number_of_boxes)
