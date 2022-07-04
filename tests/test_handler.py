import json
import os
import pytest

import cli
import graphs

def test_load_valid_file(pytestconfig):
    file_path = os.path.join(pytestconfig.rootpath, "tests", "graph.txt")
    obj = cli.getObject(file_path)
    assert isinstance(obj, dict), "Object loaded from graph.txt is not dictionary"

