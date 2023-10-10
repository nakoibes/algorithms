def check_connected(graph: dict[int, list[int]], start: int, finish: int) -> bool:
    seen_nodes = set()
    next_nodes = set()
    next_nodes.add(start)
    # next_nodes.extend(graph[start])
    seen_nodes.add(start)
    while next_nodes:
        current_node = next_nodes.pop()
        if current_node == finish:
            return True
        for node in graph[current_node]:
            if node == finish:
                return True
            if node not in seen_nodes:
                next_nodes.add(node)
                seen_nodes.add(node)


    return False





if __name__ == '__main__':
    graph = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3, 5, 6], 5: [4], 6: [4, 7, 8], 7: [6, 8], 8: [6, 7]}
    # print(*depth_search(graph, 1, 5))
    print(check_connected(graph, 4, 1))
