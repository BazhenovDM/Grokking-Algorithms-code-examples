from collections import deque

queue = deque()

graph = {}

graph["вы"] = ["Алиса", "Боб", "Клэр"]
graph["Боб"] = ["Анудж", "Пегги"]
graph["Алиса"] = ["Пегги"]
graph["Клэр"] = ["Том", "Джонни"]
graph["Анудж"] = []
graph["Пегги"] = []
graph["Том"] = []
graph["Джонни"] = []

queue += graph["вы"]


def person_is_seller(name):
    return name[-1] == 'м'


def search(name):
    queue = deque()
    queue += graph[name]
    person_list = []
    while queue:
        person = queue.popleft()
        if person in person_list:
            continue
        if person_is_seller(person):
            return person
        person_list.append(person)
        queue += graph[person]
    else:
        return None


print(search("вы"))
