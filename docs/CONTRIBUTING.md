## Contributing to LeetCode Solutions

This guide explains how to add new LeetCode problem solutions to this repository.

### Prerequisites

- Python 3.x
- CMake 3.14+
- C++17 compatible compiler
- Google Test framework

### Adding a New Solution

#### 1. Generate Problem Structure

Run the automation script from the project root:

```bash
python3 scripts/new_solution.py <problem_number> <problem-name>
```

**Example:**
```bash
python3 scripts/new_solution.py 1 two-sum
```

The script will prompt you for:
- **Difficulty**: Select Easy/Medium/Hard (defaults to Medium)
- **Topics**: Enter hashtags like `#array #hash-table` (optional)

**Generated files:**
- `src/problems/<number>_<name>/solution.h` - Solution header
- `src/problems/<number>_<name>/solution.cpp` - Implementation
- `src/problems/<number>_<name>/README.md` - Problem description
- `tests/test_<number>_<name>.cpp` - Test file
- Updates `tests/CMakeLists.txt` automatically
- Updates `docs/PROBLEM_INDEX.md` automatically

#### 2. Implement the Solution

Edit the generated files:
- `solution.h` - Define your solution class and methods
- `solution.cpp` - Implement the solution logic
- `README.md` - Add problem description and examples

#### 3. Write Tests

Add test cases in `tests/test_<number>_<name>.cpp` using Google Test framework:

```cpp
TEST_F(SolutionTest, TestCase1) {
    // Arrange
    // Act
    // Assert
}
```

#### 4. Build and Test

```bash
mkdir -p build && cd build
cmake ..
cmake --build .
ctest --verbose
```

#### 5. Commit Your Changes

```bash
git add .
git commit -m "Add solution for Problem #<number>: <Name>"
git push origin main
```

### Code Standards

- **C++ Style**: Follow modern C++17 practices
- **Naming**: Use camelCase for methods, PascalCase for classes
- **Documentation**: Include time/space complexity analysis
- **Testing**: Achieve comprehensive test coverage with edge cases

### Project Structure

```
src/problems/<number>_<name>/
├── solution.h          # Solution interface
├── solution.cpp        # Implementation
└── README.md          # Problem details

tests/
└── test_<number>_<name>.cpp  # Unit tests
```

### Getting Help

If you encounter issues with the automation script or build process, please open an issue in the repository.