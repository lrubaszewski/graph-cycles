import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def simpleCyclesTarjan(graph):
    # Algorithm description: https://ecommons.cornell.edu/handle/1813/5941

    def backtrack(start_v, curr_v):
        found = False

        point_stack.append(curr_v)
        mark[curr_v] = True
        marked_stack.append(curr_v)

        logger.debug(f"{start_v=} {curr_v=} {mark=} {marked_stack=} {point_stack=}")

        # If vertex not present in graph then it has no neighbours, return empty list
        neighbours = graph.get(curr_v, [])
        logger.debug(f"{start_v=} {curr_v=} {neighbours=}")
        for neighbour in neighbours:
            logger.debug(f"{start_v=} {curr_v=} {neighbour=}")
            if neighbour < start_v:
                neighbours.remove(neighbour)
                logger.debug(f"after delete {neighbours=}")
            elif neighbour == start_v:
                logger.debug(f"Cycle found: {point_stack=}")
                # Do not append reference to point_stack - it is constantly manipulated in this method
                # Copy it.
                simple_cycles.append(point_stack[:])
                found = True
            elif mark.get(neighbour, False) == False:
                found = backtrack(start_v, neighbour) or found

        if found is True:
            while True:
                u = marked_stack.pop()
                mark[u] = False

                if u == curr_v:
                    break
        point_stack.pop()
        return found


    logger.debug(f"Input graph: {graph}")

    # Initialization
    mark = {v: False for v in graph}
    point_stack = []
    marked_stack = []

    simple_cycles = []
    for v in graph:
        logger.debug(f"Checking vertex: {v}")
        backtrack(v, v)
        while len(marked_stack) > 0:
            u = marked_stack.pop()
            mark[u] = False

    return simple_cycles

