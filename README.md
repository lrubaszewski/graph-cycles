# Overview
Finds all cycles in given file.

# Usage
```bash
./src/cli.py tests/graph.txt
```
or
```bash
echo "{'orange': ['monkey', 'banana'], 'monkey': ['cow', 'orange'], 'banana': ['mango', 'monkey']}" | ./src/cli.py
```

# Testing
```bash
python3 -m venv venv
venv/bin/pip install -r requirements-devel.txt
venv/bin/pytest
```
