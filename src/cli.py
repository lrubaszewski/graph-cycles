#!/usr/bin/env python3.8
import json
import logging
import sys

import graphs


def getObject(fname):
    if fname not in [None, "-"]:
        fd = open(fname, "r")
    else:
        fd = sys.stdin
    obj = json.load(fd)
    if fd is not sys.stdin:
        fd.close()
    return obj


def main():
    logging.basicConfig(
        stream=sys.stderr,
        format="%(levelname)s:%(name)s [%(funcName)s():%(lineno)s] - %(message)s",
    )

    fname = sys.argv[1] if len(sys.argv) > 1 else None

    cycles = graphs.simpleCyclesTarjan(getObject(fname))
    print("Cycles found:")
    for c in cycles:
        print(f"{c}")


if __name__ == "__main__":
    main()
