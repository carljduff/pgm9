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

    return swapped_count, compared_count

def selection_sort(my_list):
    n = len(my_list)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if my_list[min_idx] > my_list[j]:
                min_idx = j

        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]



if __name__ == '__main__':
    main()

