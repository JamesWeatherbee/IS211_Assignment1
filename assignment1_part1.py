#!/usr/bin/python
# -*- coding: utf-8 -*-

class ListDivideException(Exception):
    pass


def listDivide(numbers, divide=2):
    """
    Counts how many numbers in a given list are divisible by a given parameter

    :param numbers: int
        User provided list of numbers
    :param divide: int
        User provided divisor. Default = 2

    :return:
    int
        Amount of numbers from the numbers list divisible by the divide parameter
    """
    newList = []
    for i in numbers:
        if i % divide == 0:
            newList.append(i)
    return len(newList)


def testListDivide():
    """
    Tests the function listDivide for errors
    """
    listDivide([1, 2, 3, 4, 5])
    listDivide([2, 4, 6, 8, 10])
    listDivide([30, 54, 63, 98, 100], divide=10)
    listDivide([])
    listDivide([1, 2, 3, 4, 5], 1)


if __name__ == '__main__':
    try:
        testListDivide()
    except TypeError:
        print('Invalid parameters')
