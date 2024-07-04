#!/usr/bin/python3
"""Module for the lockbox challenge"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened
    """
    n = len(boxes)
    visited_boxes = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box not in visited_boxes:
            visited_boxes.add(current_box)
            for key in boxes[current_box]:
                if key < n:
                    stack.append(key)

    return len(visited_boxes) == n
