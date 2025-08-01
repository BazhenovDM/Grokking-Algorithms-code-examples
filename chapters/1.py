def binary_search(locker: list, value) -> int | None:
    low = 0
    high = len(locker) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = locker[mid]
        if guess == value:
            return mid
        elif guess < value:
            low = mid + 1
        else:
            high = mid - 1
    return None
