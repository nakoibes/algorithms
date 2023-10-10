def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra_search(graph, costs, parents):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n, n_cost in neighbors.items():
            new_cost = cost + n_cost
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return parents


def show_path(parents):
    path = ["fin"]
    current = parents["fin"]
    while current != "start":
        path.append(current)
        current = parents[current]
    path.append('start')
    path.reverse()
    return path


if __name__ == '__main__':
    graph = dict()

    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph['a'] = {}
    graph['b'] = {}
    graph['fin'] = {}
    graph["a"]["fin"] = 1
    graph['b']["a"] = 3
    graph["b"]["fin"] = 5
    infinity = float("inf")
    costs = dict()
    costs['a'] = 6
    costs['b'] = 2
    costs['fin'] = infinity
    parents = dict()
    parents['a'] = "start"
    parents['b'] = "start"
    parents['fin'] = None


    result = dijkstra_search(graph, costs, parents)
    print(show_path(result))



# def find_lowest_weight(nodes: dict, ready_nodes: set[int]):
#     lowest_node = None
#     lowest_weight = float("inf")
#     for node, weight in nodes.items():
#         if weight < lowest_weight and node not in ready_nodes:
#             lowest_node = node
#             lowest_weight = weight
#     return lowest_node
#
#
# def dij(graph: dict[int:list[tuple[int, int]]], start: int, finish: int):
#     parents = dict()
#     path = list()
#     ready_nodes = set()
#     weights = {}
#     for node in graph:
#         weights[node] = float("inf")
#     weights[start] = 0
#     while True:
#         current_node = find_lowest_weight(weights, ready_nodes)
#         ready_nodes.add(current_node)
#         for node in graph[current_node]:
#             new_weight = weights[current_node] + node[1]
#             if new_weight < weights[node[0]]:
#                 weights[node[0]] = new_weight
#                 parents[node[0]] = current_node
#         if finish in ready_nodes:
#             break
#
#     node = finish
#     path.append(finish)
#     while True:
#         parent = parents[node]
#         path.append(parent)
#         node = parent
#         if parent == start:
#             break
#     path.reverse()
#     print(path)
#     return weights[finish]
#
# #
# if __name__ == '__main__':
#     graph = {1: [(2, 6), (3, 2)], 2: [(4, 1)], 3: [(2, 3), (4, 5)], 4: []}
#     graph1 = {1: [(2, 4), (3, 10)], 2: [(5, 21)], 3: [(4, 5), (6, 8)], 4: [(5, 5)], 5: [(7, 4)], 6: [(5, 12)], 7: []}
#     graph2 = {1: [(2, 1), (3, 2)], 2: [(4, 3)], 3: [(4, 1)], 4: []}
#     graph3 = {1: [(2, 10)], 2: [(3, 20)], 3: [(5, 30), (4, 1)], 4: [(2, 1)], 5: []}
#     print(dij(graph3, 1, 5))
