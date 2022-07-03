import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def simple_cycles(graph):
    simple_cycles = []
    logger.debug(f"Input graph: {graph}")

    logger.debug(f"Found cycles {simple_cycles}")
    return simple_cycles
