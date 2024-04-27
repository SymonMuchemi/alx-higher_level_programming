#!/usr/bin/python3
# Finds the peak in a list

def find_peak(list_of_integers):
    """ finds a peak in the list and print it out """
    if len(list_of_integers) == 0:
        print("None")
        return

    peaks = []
    peaks.append(list_of_integers[0])
    for index in range(1, len(list_of_integers) - 1):
        current = list_of_integers[index]
        prev = list_of_integers[index - 1]
        nxt = list_of_integers[index + 1]

        if current > prev and current > nxt:
            peaks.append(current)
    peaks.append(list_of_integers[-1])

    print(max(peaks))
