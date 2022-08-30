#!/usr/bin/python
"""flatten.py - extended utils
"""


def flattenList(nestedList):
    """
    Flatten nested list of items
    1st case : empty array >> return array
    2nd case : item 0 is a not list >> return nested list at index 0 AND flatten list of the rest of the nestedlist
    3rd case : item 0 is a list >> return flatten list of nested items(index 0) AND nested list of items (index 1 and more)
    :param nestedList:
    :return: flattened list
    """

    if len(nestedList) == 0:
        return nestedList
    if not isinstance(nestedList[0], list):
        return nestedList[:1] + flattenList(nestedList[1:])
    else:
        return flattenList(nestedList[0]) + flattenList(nestedList[1:])
