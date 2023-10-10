from collections import deque


def check_connected(graph, start, finish):
    next_nodes = deque()
    seen_nodes = set()
    next_nodes.appendleft(start)
    while next_nodes:
        current_node = next_nodes.pop()
        if current_node == finish:
            return True
        for node in graph[current_node]:
            if node == finish:
                return True
            if node not in seen_nodes:
                next_nodes.appendleft(node)
                seen_nodes.add(node)

    return False


# def check_connected_directed(graph, start, finish) -> True:
#     next_nodes = deque()
#     next_nodes.appendleft(start)
#     while next_nodes:
#         current_node = next_nodes.pop()
#         if current_node == finish:
#             return True
#         for node in graph[current_node]:
#             if node == finish:
#                 return True
#             next_nodes.extendleft(graph[node])
#
#     return False

def _find_path_width(graph: dict[int, list[int]], parents: dict[int, int], start: int, finish: int) -> bool:
    seen_nodes = set()
    next_nodes = deque()
    seen_nodes.add(start)
    next_nodes.appendleft(start)
    while next_nodes:
        current_node = next_nodes.pop()
        if current_node == finish:
            return True
        for node in graph[current_node]:
            if node not in seen_nodes:
                next_nodes.appendleft(node)
                seen_nodes.add(node)
                parents[node] = current_node
    return False


def find_path_width(graph: dict[int, list[int]], start: int, finish: int) -> list[int]:
    parents = dict()
    path = list()
    if _find_path_width(graph, parents, start, finish):
        current = finish
        path.append(finish)
        while current != start:
            parent = parents[current]
            path.append(parent)
            current = parent

        # path.append(start)
        path.reverse()
        return path
    else:
        return list()


def width_search(graph, start, finish) -> bool:
    searched = []
    search_deque = deque()
    search_deque += graph[start]
    while search_deque:
        person = search_deque.popleft()
        if person == finish:
            print(f"{person}!")
            return True
        elif person not in searched:
            search_deque += graph[person]
        searched.append(person)
    return False


if __name__ == '__main__':
    # graph = {}
    # graph['you'] = ['alice', 'bob', 'claire']
    # graph['bob'] = ['anuj', 'peggy']
    # graph['alice'] = ['peggy']
    # graph['claire'] = ['thom', 'jonny']
    # graph['anuj'] = []
    # graph['peggy'] = []
    # graph['thom'] = []
    # graph['jonny'] = []
    # width_search(graph, 'you', 'thom')

    graph = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3, 5, 6], 5: [4], 6: [4, 7, 8], 7: [6, 8], 8: [6, 7]}
    directed_graph = {1: [2, 3], 2: [4], 3: [4], 4: [5, 6], 5: [], 6: [7, 8], 7: [8], 8: []}
    # for i in range(1,9):
    #     for j in range(i+1,9):
    #         print(i,j,check_connected(directed_graph,i,j))
    # print(check_connected(directed_graph,6,1))
    # print(check_connected(directed_graph, 1, 7))
    print(find_path_width(graph,1,6))