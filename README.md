# Overview
Finds all cycles in given file.

# Usage
```bash
./src/cli.py tests/graph.txt
```
or
```bash
echo '{"orange": ["monkey", "banana"], "monkey": ["cow", "range"], "banana": ["mango", "monkey"]}' | ./src/cli.py
```

# Testing
```bash
make test
```

New test files might be added by creating another test files in tests/ folder.
File must follow this naming convention: `graph*.txt`
Eg.
  `tests/graph5.txt`

# Format code
```bash
make black
```

# Prepare for pull-request
```bash
make pr
```
