# Scripts

Automation tools for scaffolding new problem solutions.

## Usage

```bash
python3 new_solution.py <problem-number> <problem-name>
```

### Arguments
- `problem-number`: LeetCode problem number (positive integer)
- `problem-name`: Problem name in kebab-case (e.g., `two-sum`, `unique-paths`)

### Example
```bash
python3 new_solution.py 1 two-sum
```

This creates:
- `src/problems/two-sum/solution.h`
- `src/problems/two-sum/solution.cpp`
- `src/problems/two-sum/README.md`
- `tests/test_two_sum.cpp`

And updates `tests/CMakeLists.txt` automatically.

