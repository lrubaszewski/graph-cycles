import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def simpleCyclesTarjan(graph):
    """
    Function returns a list of all simple cycles in a given directed graph.
    Algorithm description: https://ecommons.cornell.edu/handle/1813/5941

    :param graph: dict of keys (vertexes) and values (vertexes' neighbours)
    :return: list of simple cycles found in graph
    """

    def backtrack(start_v, curr_v):
        found = False

        point_stack.append(curr_v)
        mark[curr_v] = True
        marked_stack.append(curr_v)

        logger.debug(f"{start_v=} {curr_v=} {marked_stack=} {point_stack=}")

        # If vertex not present in graph then it has no neighbours, return empty list
        neighbours = graph.get(curr_v, [])
        logger.debug(f"{start_v=} {curr_v=} {neighbours=}")
        for neighbour in neighbours:
            logger.debug(f"{start_v=} {curr_v=} {neighbour=}")
            if neighbour < start_v:
                graph[neighbour] = []
            elif neighbour == start_v:
                logger.debug(f">>>> Cycle found: {point_stack=}")
                # Do not append reference to point_stack - it is constantly manipulated in this method
                # Copy it.
                simple_cycles.append(point_stack[:])
                found = True
            elif not mark.get(neighbour, False):
                found = backtrack(start_v, neighbour) or found

        logger.debug(f"{start_v=} {curr_v=} {neighbours=} {point_stack=}")

        if found is True:
            while True:
                u = marked_stack.pop()
                mark[u] = False

                if u == curr_v:
                    break
        point_stack.pop()
        return found

    logger.debug(f"Input graph: {graph}")
    # Sort graph by vertexes, algorithms assumes iterating vertexes in ascending order
    graph = dict(sorted(graph.items()))
    logger.debug(f"Sorted graph: {graph}")

    # Initialization
    mark = {v: False for v in graph}
    point_stack = []
    marked_stack = []

    simple_cycles = []
    # We iterate over a list of keys (vertexes) instead of directly over keys (vertexes) in dict
    # in order to avoid error:
    #   RuntimeError: dictionary changed size during iteration
    # when setting the empty list for key (vertex) in backtrack method
    for v in list(graph):
        logger.debug(f"Checking vertex: {v}")
        backtrack(v, v)
        while len(marked_stack) > 0:
            u = marked_stack.pop()
            mark[u] = False

    return simple_cycles
