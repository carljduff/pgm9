def main():
    pass

def bubble_sort(my_list):
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

    return my_list, swapped_count, compared_count

def selection_sort(my_list):
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

    return my_list, swapped_count, compared_count

quick_sort_count = 0

def quick_sort(my_list):
    global quick_sort_count

    less = []
    equal = []
    greater = []

    if len(my_list) > 1:
        quick_sort_count += 1
        pivot = my_list[0]

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

        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return my_list

if __name__ == '__main__':
    main()

