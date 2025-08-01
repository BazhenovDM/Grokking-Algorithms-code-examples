from collections import deque
from os import listdir
from os.path import isfile, join


def print_names(start_dir):
    queue = deque()
    queue.append(start_dir)
    while queue:
        dir = queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(file)
            else:
                queue.append(fullpath)


print_names("/")
