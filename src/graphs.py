import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def simpleCyclesTarjan(in_graph):
    # Algorithm description: https://ecommons.cornell.edu/handle/1813/5941
    simple_cycles = []
    graph = []
    map_graph_to_int = {}
    map_int_to_graph = {}
    graph_len = 0

    def mapGraphToInt(in_graph):
        # Algorith requires graph vertex to be represented by array (of vertexes) of arrays of integers (adjacent vertexes)
        # Eg.
        #  graph[0] = [1, 4, 2] - vertex 0 neighbours: 1, 4, 2
        graph = []
        idx = 0

        # Assign unique integer values for graph items
        for vertex, neighbours in in_graph.items():
            for item in [vertex, *neighbours]:
                if item not in map_graph_to_int:
                    map_graph_to_int[item] = idx
                    map_int_to_graph[idx] = item
                    idx += 1

        # Translate an input graph into array of arrays
        for idx, vertex in sorted(map_int_to_graph.items()):
            neighbours = list(map(lambda item: map_graph_to_int[item], in_graph.get(vertex, [])))
            graph.append(neighbours)
        graph_len = len(graph)
        return graph

    def backtrack(start_v, curr_v):
        found = False

        point_stack.append(curr_v)
        mark[curr_v] = True
        marked_stack.append(curr_v)

        logger.debug(f"{start_v=} {curr_v=} {mark=} {marked_stack=} {point_stack=} {graph[curr_v]=}")

        neighbours = graph[curr_v]
        logger.debug(f"{start_v=} {curr_v=} {neighbours=}")
        for neighbour in neighbours:
            logger.debug(f"{start_v=} {curr_v=} {neighbour=}")
            if neighbour < start_v:
                neighbours.remove(neighbour)
                logger.debug(f"after delete {neighbours=}")
            elif neighbour == start_v:
                logger.debug(f"Cycle found: {point_stack=}")
                simple_cycles.append(
                        list(map(lambda key: map_int_to_graph[key], point_stack))
                    )
                found = True
            elif mark[neighbour] == False:
                found = backtrack(start_v, neighbour) or found

        if found is True:
            while True:
                u = marked_stack.pop()
                mark[u] = False

                if u == curr_v:
                    break
        point_stack.pop()
        return found


    logger.debug(f"Input graph: {in_graph}")

    graph = mapGraphToInt(in_graph)
    graph_len = len(graph)
    logger.debug(f"Mapped graph {graph}")

    # Initialization
    mark = {idx: False for idx in range(graph_len)}
    point_stack = []
    marked_stack = []

    for v in range(graph_len):
        logger.debug(f"start_vertex={v}")
        cycle_found = backtrack(v, v)
        while len(marked_stack) > 0:
            u = marked_stack.pop()
            mark[u] = False

    return simple_cycles

