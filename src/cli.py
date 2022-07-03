#!/usr/bin/env python3.8
import sys
import json
import logging
import graphs

def getObject(fname):
    if fname not in [ None, '-' ]:
        fd = open(fname, "r")
    else:
        fd = sys.stdin
    obj = json.load(fd)
    if fd is not sys.stdin:
        fd.close()
    return obj

def main():
    logging.basicConfig(stream=sys.stderr)

    fname = sys.argv[1] if len(sys.argv) > 1 else None
    cycles = graphs.simple_cycles(getObject(fname))

if __name__ == '__main__':
    main()

