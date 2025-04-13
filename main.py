import time
import sys
import random
import matplotlib.pyplot as plt
import numpy as np

sys.setrecursionlimit(6000)

quick_sort_count = 0
quick_sort_wall_time = 0
quick_sort_wall_start = 0
quick_sort_cpu_time = 0
quick_sort_cpu_start = 0
depth_of_recursion = 0

def create_list(size):
    my_list = []

    for num in range(0, size):
        my_list.append(random.randrange(50001))

    return f"Creating an array of size {size}", my_list

def list_info(cpu_time, wall_time, complexity):
    print(f'''
    
    Execution Time: {cpu_time} milliseconds
    Wallclock Time: {wall_time} seconds
    Complexity: {complexity}
    
    ''')

def main():
    sorts = ("Bubble Sort", "Selection Sort", "Quicksort")
#-----------------1000-----------------------------------------------
    print_statement, list_one_thousand = create_list(1000)
    print()
    print(print_statement)

    bubble_swapped_count_1000, bubble_compared_count_1000, bubble_wall_time_1000, bubble_cpu_time_1000 = bubble_sort(list_one_thousand)

    print(f'*** {sorts[0]} ***')
    list_info(bubble_cpu_time_1000, bubble_wall_time_1000, (bubble_swapped_count_1000 + bubble_compared_count_1000))


    selection_swapped_count_1000, selection_compared_count_1000, selection_wall_time_1000, selection_cpu_time_1000 = selection_sort(list_one_thousand)

    print(f'*** {sorts[1]} ***')
    list_info(selection_cpu_time_1000, selection_wall_time_1000, (selection_swapped_count_1000 + selection_compared_count_1000))

    quick_sort(list_one_thousand)
    print(f'*** {sorts[2]} (Recursive) ***')
    list_info(quick_sort_cpu_time, quick_sort_wall_time, quick_sort_count)

#--------------5000-------------------------------------------
    print_statement, list_five_thousand = create_list(5000)
    print()
    print(print_statement)

    bubble_swapped_count_5000, bubble_compared_count_5000, bubble_wall_time_5000, bubble_cpu_time_5000 = bubble_sort(list_five_thousand)

    print(f'*** {sorts[0]} ***')
    list_info(bubble_cpu_time_5000, bubble_wall_time_5000, (bubble_swapped_count_5000 + bubble_compared_count_5000))

    selection_swapped_count_5000, selection_compared_count_5000, selection_wall_time_5000, selection_cpu_time_5000 = selection_sort(list_five_thousand)

    print(f'*** {sorts[1]} ***')
    list_info(selection_cpu_time_5000, selection_wall_time_5000, (selection_swapped_count_5000 + selection_compared_count_5000))

    quick_sort(list_five_thousand)
    print(f'*** {sorts[2]} (Recursive) ***')
    list_info(quick_sort_cpu_time, quick_sort_wall_time, quick_sort_count)

# --------------10,000-------------------------------------------
    print_statement, list_ten_thousand = create_list(10000)
    print()
    print(print_statement)

    bubble_swapped_count_10000, bubble_compared_count_10000, bubble_wall_time_10000, bubble_cpu_time_10000 = bubble_sort(list_ten_thousand)

    print(f'*** {sorts[0]} ***')
    list_info(bubble_cpu_time_10000, bubble_wall_time_10000, (bubble_swapped_count_10000 + bubble_compared_count_10000))

    selection_swapped_count_10000, selection_compared_count_10000, selection_wall_time_10000, selection_cpu_time_10000 = selection_sort(list_ten_thousand)

    print(f'*** {sorts[1]} ***')
    list_info(selection_cpu_time_10000, selection_wall_time_10000, (selection_swapped_count_10000 + selection_compared_count_10000))

    quick_sort(list_ten_thousand)
    print(f'*** {sorts[2]} (Recursive) ***')
    list_info(quick_sort_cpu_time, quick_sort_wall_time, quick_sort_count)

# --------------50,000-------------------------------------------
    print_statement, list_fifty_thousand = create_list(50000)
    print()
    print(print_statement)

    bubble_swapped_count_50000, bubble_compared_count_50000, bubble_wall_time_50000, bubble_cpu_time_50000 = bubble_sort(list_fifty_thousand)

    print(f'*** {sorts[0]} ***')
    list_info(bubble_cpu_time_50000, bubble_wall_time_50000, (bubble_swapped_count_50000 + bubble_compared_count_50000))

    selection_swapped_count_50000, selection_compared_count_50000, selection_wall_time_50000, selection_cpu_time_50000 = selection_sort(list_fifty_thousand)

    print(f'*** {sorts[1]} ***')
    list_info(selection_cpu_time_50000, selection_wall_time_50000, (selection_swapped_count_50000 + selection_compared_count_50000))

    quick_sort(list_fifty_thousand)
    print(f'*** {sorts[2]} (Recursive) ***')
    list_info(quick_sort_cpu_time, quick_sort_wall_time, quick_sort_count)


    wall_clock_times = {
        '1000': (bubble_wall_time_1000, selection_wall_time_1000, quick_sort_wall_time),
        '5000': (bubble_wall_time_5000, selection_wall_time_5000, quick_sort_wall_time),
        '10000': (bubble_wall_time_10000, selection_wall_time_10000, quick_sort_wall_time),
        '50000': (bubble_wall_time_50000, selection_wall_time_50000, quick_sort_wall_time),
    }

    complexities = {
        '1000': ((bubble_swapped_count_1000 + bubble_compared_count_1000), (selection_swapped_count_1000 + selection_compared_count_1000), quick_sort_count),
        '5000': ((bubble_swapped_count_5000 + bubble_compared_count_5000), (selection_swapped_count_5000 + selection_compared_count_5000), quick_sort_count),
        '10000': ((bubble_swapped_count_10000 + bubble_compared_count_10000), (selection_swapped_count_10000 + selection_compared_count_10000), quick_sort_count),
        '50000': ((bubble_swapped_count_50000 + bubble_compared_count_50000), (selection_swapped_count_50000 + selection_compared_count_50000), quick_sort_count),
    }

    exec_times = {
        '1000': (bubble_cpu_time_1000, selection_cpu_time_1000, quick_sort_cpu_time),
        '5000': (bubble_cpu_time_5000, selection_cpu_time_5000, quick_sort_cpu_time),
        '10000': (bubble_cpu_time_10000, selection_cpu_time_10000, quick_sort_cpu_time),
        '50000': (bubble_cpu_time_50000, selection_cpu_time_50000, quick_sort_cpu_time),
    }

    width = 0.25

    x = np.arange(len(sorts))  # the label locations

    fig, ax = plt.subplots(3, 1, layout='constrained')

    fig.set_figheight(8)

    #  Wall Clock Times

    multiplier = 0

    for attribute, measurement in wall_clock_times.items():
        offset = width * multiplier
        rects = ax[0].bar(x + offset, measurement, width, label=attribute)
        ax[0].bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-ax[0]is tick labels, etc.

    ax[0].set_ylabel('Wall Clock Time\n(seconds)')
    ax[0].set_title('Sort Comparisons')
    ax[0].set_xticks(x + width, sorts)
    ax[0].legend(loc='upper left', ncols=4)

    biggest = my_max(wall_clock_times)

    ax[0].set_ylim(0, biggest * 1.40)

    # Complexities

    multiplier = 0

    x = np.arange(len(sorts))  # the label locations

    for attribute, measurement in complexities.items():
        offset = width * multiplier
        rects = ax[1].bar(x + offset, measurement, width, label=attribute)
        ax[1].bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-ax[0]is tick labels, etc.

    ax[1].set_ylabel('Complexity')
    # ax[1].set_title('Sort Comparisons')
    ax[1].set_xticks(x + width, sorts)
    ax[1].legend(loc='upper left', ncols=4)

    biggest = my_max(complexities)

    ax[1].set_ylim(0, biggest * 1.40)

    # execution times

    multiplier = 0

    for attribute, measurement in exec_times.items():
        offset = width * multiplier
        rects = ax[2].bar(x + offset, measurement, width, label=attribute)
        ax[2].bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-ax[0]is tick labels, etc.

    ax[2].set_ylabel('Execution Time\n(milliseconds)')
    ax[2].set_title('Sort Comparisons')
    ax[2].set_xticks(x + width, sorts)
    ax[2].legend(loc='upper left', ncols=4)

    biggest = my_max(exec_times)

    ax[2].set_ylim(0, biggest * 1.40)

    fig.savefig('graphs.png')

def my_max(dict_of_lists):
    keys = dict_of_lists.keys()
    k = [*keys]
    firstdictkey = k[0]
    firstlist = dict_of_lists[firstdictkey]
    firstvalue = firstlist[0]

    max = firstvalue

    for count in dict_of_lists.keys():
        for value in dict_of_lists[count]:
            if value > max:
                max = value
    return max


def bubble_sort(my_list):
    wall_start = time.time()
    cpu_start = time.process_time()

    n = len(my_list)
    swapped_count = 0
    compared_count = 0

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            compared_count += 1
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j + 1], my_list[j]
                swapped = True
                swapped_count += 1

        if not swapped:
            break

    wall_end = time.time()
    cpu_end = time.process_time()

    wall_time = wall_end - wall_start
    cpu_time = cpu_end - cpu_start


    return swapped_count, compared_count, wall_time, cpu_time

def selection_sort(my_list):
    wall_start = time.time()
    cpu_start = time.process_time()

    n = len(my_list)
    swapped_count = 0
    compared_count = 0

    for i in range(n):
        min_idx = i

        for j in range(i+1, n):
            compared_count += 1
            if my_list[min_idx] > my_list[j]:
                min_idx = j

        if min_idx != i:
            my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
            swapped_count += 1

    wall_end = time.time()
    cpu_end = time.process_time()

    wall_time = wall_end - wall_start
    cpu_time = cpu_end - cpu_start

    return swapped_count, compared_count, wall_time, cpu_time

def quick_sort(my_list):
    global quick_sort_count, quick_sort_wall_time, quick_sort_wall_start, quick_sort_cpu_time, quick_sort_cpu_start, depth_of_recursion

    if depth_of_recursion == 0:
        quick_sort_wall_start = time.time()
        quick_sort_cpu_start = time.process_time()

    depth_of_recursion += 1

    less = []
    equal = []
    greater = []

    if len(my_list) > 1:
        quick_sort_count += 1
        pivot = my_list[random.randrange(len(my_list))]

        for x in my_list:
            if x < pivot:
                less.append(x)
                quick_sort_count += 1
            if x == pivot:
                equal.append(x)
                quick_sort_count += 1
            if x > pivot:
                greater.append(x)
                quick_sort_count += 1

        sorted_list = quick_sort(less) + equal + quick_sort(greater)
    else:
        sorted_list = my_list

    depth_of_recursion -= 1

    if depth_of_recursion == 0:
        wall_end = time.time()
        cpu_end = time.process_time()
        quick_sort_wall_time = wall_end - quick_sort_wall_start
        quick_sort_cpu_time = cpu_end - quick_sort_cpu_start

    return sorted_list

if __name__ == '__main__':
    main()

