#!/usr/bin/python3
""" function finds the peak value in a list on integers

    The idea is to first sort the array using merge sort which has
    a time complexity of O(n log n) the retrieve the last element, which is
    the largest integer element in the array
    """


def merge_sort(arr):
    """sorts the array using divide and conquer

    Args:
        arr (int): the array of integer elements

    Returns:
        arr: a sorted version of the initial list
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    """combines two arrays to form one

    Args:
        left (arr): a subarray
        right (arr): another subarray

    Returns:
        arr: combined array
    """
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


def find_peak(list_of_integers):
    """finds the peak in a list

    Args:
        list_of_integers (int): the array of integers

    Returns:
        int: the largest integer in the list
    """
    if len(list_of_integers) == 0:
        return None

    # sort the array and return the last element
    return merge_sort(list_of_integers)[-1]
