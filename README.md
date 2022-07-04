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

New test files might be added by creating another test files in tests/ folder.
File must follow this naming convention: `graph*.txt`
Eg.
  `tests/graph5.txt`
