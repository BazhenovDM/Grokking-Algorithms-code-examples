def countdown(count: int) -> None:
    print(count)
    if count <= 1:
        return
    countdown(count - 1)


def fact(x: int) -> int:
    if x == 1:
        return 1
    return x * fact(x - 1)
