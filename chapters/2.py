def find_smallest(arr: list) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:
    new_arr = []
    length = len(arr)
    for i in range(length):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def selection_sort2(arr: list) -> list:
    length = len(arr)
    for i in range(length - 1):
        smallest_ind = i
        for j in range(i + 1, length):
            if arr[j] < arr[smallest_ind]:
                smallest_ind = j
        if smallest_ind != i:
            arr[i], arr[smallest_ind] = arr[smallest_ind], arr[i]
    return arr
