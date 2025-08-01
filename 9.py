graph = {
    "начало": {
        "a": 6,
        "b": 2
    },
    "a": {
        "конец": 1,
    },
    "b": {
        "a": 3,
        "конец": 5
    },
    "конец": {},
}

infinity = float("inf")

costs = {
    "a": 6,
    "b": 2,
    "конец": infinity,
}

parents = {
    "a": "начало",
    "b": "начало",
    "конец": None
}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost_node = node
            lowest_cost = cost
    return lowest_cost_node


def dijkstra_algorithm():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return costs["конец"], parents


cost, path = dijkstra_algorithm()
print(cost, path)
