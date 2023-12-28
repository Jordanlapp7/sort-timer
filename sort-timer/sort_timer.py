# Author: Jordan Lapp
# GitHub username: JordanLapp7
# Date: 8/5/2023
# Description: Graphs the sorting times of two sorting algorithms on different list lengths.

import time
import random
from matplotlib import pyplot
from functools import wraps


def sort_timer(func):
    """Decorator function that times how many seconds it takes decorated function to run."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Measures time for function to run."""
        before = time.perf_counter()
        func(*args, **kwargs)
        after = time.perf_counter()
        return after - before
    return wrapper


@sort_timer
def bubble_sort(a_list):
    """Sorts a_list in ascending order."""
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """Sorts a_list in ascending order"""
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
            a_list[pos + 1] = value


def make_lists_of_sort_times(sort_1, sort_2, lengths):
    """Compares sort times of two sort functions of random lists of lengths defined in lengths list"""
    sort_1_times = []
    sort_2_times = []
    for length in lengths:
        list_1 = []
        for _ in range(length):
            list_1.append(random.randint(1, 10000))
        list_2 = list(list_1)
        sort_1_time = sort_1(list_1)
        sort_2_time = sort_2(list_2)
        sort_1_times.append(sort_1_time)
        sort_2_times.append(sort_2_time)
    times = (sort_1_times, sort_2_times)
    return times


def compare_sorts(sort_1, sort_2):
    """Runs make_lists_of_sort_times function on ten incrementing lengths and compares values on a graph."""
    lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    times = make_lists_of_sort_times(sort_1, sort_2, lengths)
    pyplot.plot(lengths, times[0], 'ro--', linewidth=2, label='Bubble Sort')
    pyplot.plot(lengths, times[1], 'go--', linewidth=2, label='Insertion Sort')
    pyplot.xlabel("List Length")
    pyplot.ylabel("Time")
    pyplot.legend(loc='upper left')
    pyplot.show()


compare_sorts(bubble_sort, insertion_sort)
