def rec_sum(arr: list) -> int:
    if len(arr) == 1:
        return arr[0]
    return arr.pop() + rec_sum(arr)


def count(arr: list) -> int:
    if not arr:
        return 0
    return 1 + count(arr[1:])


def max_value(arr: list, value=None) -> list:
    if not arr:
        return value
    if not value or value < arr[0]:
        value = arr[0]
    return max_value(arr[1:], value)


def max_value2(arr: list) -> int:
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_value2(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array
    op = array[0]
    less = [i for i in array[1:] if i <= op]  # в книге стоит знак <, однако тогда пропадают одинаковые числа
    greater = [i for i in array[1:] if i > op]
    return quick_sort(less) + [op] + quick_sort(greater)


def quick_sort2(array: list) -> list:
    if len(array) < 2:
        return array
    op = array[len(array) // 2]
    lower = [i for i in array if i < op]
    middle = [i for i in array if i == op]
    higher = [i for i in array if i > op]
    return quick_sort2(lower) + middle + quick_sort2(higher)


# мои потуги в реализации рекурсивного бинарного поиска
def binary_search(array: list, value, low_change=0) -> int | None:
    if len(array) == 0:
        return None
    mid = (len(array) - 1) // 2
    guess = array[mid]
    if len(array) == 1 or guess == value:
        return mid + low_change if guess == value else None
    if guess < value:
        low_change += mid + 1
        return binary_search(array[mid + 1:], value, low_change)
    elif guess > value:
        return binary_search(array[:mid], value, low_change)


def binary_search2(arr: list, low: int, high: int, value) -> int | None:
    mid = (low + high) // 2
    guess = arr[mid]
    if high == low or guess == value:
        return mid if value == guess else None
    elif guess < value:
        return binary_search2(arr, mid + 1, high, value)
    else:
        return binary_search2(arr, low, mid - 1, value)
