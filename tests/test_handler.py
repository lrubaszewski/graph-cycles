import glob
import json
import os

import cli
import graphs
import networkx
import pytest


def test_load_invalid_file(pytestconfig):
    with pytest.raises(json.decoder.JSONDecodeError):
        file_path = os.path.join(pytestconfig.rootpath, "tests", "empty.txt")
        obj = cli.getObject(file_path)


def rotate(l, n):
    # shift list by given length
    return l[n:] + l[:n]


def are_cycles_equal(cycles, ref_cycles):
    # Cycles returned by Tarjan's algorithm and networkx.simple_cycles might be in different order.
    # Therefore dedicated comparison method required.
    print(f"Comparing cycles:\n{cycles=}\n{ref_cycles=}")
    if len(cycles) != len(ref_cycles):
        return False

    equal_cycles_cnt = 0

    for c in cycles:
        print(f"Cycle {c=}")
        for r in ref_cycles:
            print(f"Compare {c=} and {r=}")
            if len(r) == len(c) and c[0] in r:
                # rotate the reference cycle so both cycles start from c[0]
                rotated = rotate(r, r.index(c[0]))
                print(f"Compare {c=} and {rotated=} rotation={-r.index(c[0])}")

                if c == rotated:
                    print(f"Cycles {c=} and {r=} are equal")
                    # remove cycle r, we no longer need it to compare
                    ref_cycles.remove(r)
                    equal_cycles_cnt += 1
                    break
                else:
                    continue

    print(
        f"Found equal cycles: {equal_cycles_cnt}, required equal cycles: {len(cycles)}"
    )
    if equal_cycles_cnt != len(cycles):
        return False

    return True


def pytest_generate_tests(metafunc):
    if "graph_file" in metafunc.fixturenames:
        this_dir = os.path.dirname(os.path.abspath(metafunc.module.__file__))
        file_list = sorted(glob.glob(os.path.join(this_dir, "graph*.txt")))
        metafunc.parametrize("graph_file", file_list)


def test_simple_cycles(graph_file):
    """
    Function performs following:
    - read a graph from given graph file
    - gets the list of the simple cycles
    - compare calculated list of cycles with the cycles returned by networkx.DiGraph

    :param graph_file: a parametrized fixture with the list of graph test files
    :return:
    """
    obj = cli.getObject(graph_file)
    assert isinstance(obj, dict), "Object loaded from graph.txt is not dictionary"

    print(f"{graph_file=}")
    graph = networkx.DiGraph(obj)
    ref_cycles = sorted(list(networkx.simple_cycles(graph)))
    print(f"{ref_cycles=}")

    cycles = graphs.simpleCyclesTarjan(obj)
    print(f"{cycles=}")

    cycles_equal = are_cycles_equal(cycles, ref_cycles)
    print(f"{cycles_equal=}")

    assert cycles_equal, "Invalid cycles found"
