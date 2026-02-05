#!/usr/bin/env python3
import os
import sys
import re
from datetime import datetime

from path import Path


def kebab_to_pascal(name):
    """Convert kebab-case to PascalCase"""
    return ''.join(word.capitalize() for word in name.split('-'))

def kebab_to_snake(name):
    """Convert kebab-case to snake_case"""
    return name.replace('-', '_')

def validate_inputs(problem_num, problem_name):
    """Validate problem number and name"""
    try:
        num = int(problem_num)
        if num <= 0:
            print(f"Error: Problem number must be positive, got {num}")
            return False
    except ValueError:
        print(f"Error: Problem number must be an integer, got '{problem_num}'")
        return False

    if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', problem_name):
        print(f"Error: Problem name must be kebab-case, got '{problem_name}'")
        return False

    return True

def prompt_difficulty():
    """Prompt user for difficulty level"""
    print("\nSelect difficulty:")
    print("  1. Easy")
    print("  2. Medium (default)")
    print("  3. Hard")
    choice = input("Enter choice (1-3) or press Enter for Medium: ").strip()

    difficulty_map = {'1': 'Easy', '2': 'Medium', '3': 'Hard', '': 'Medium'}
    return difficulty_map.get(choice, 'Medium')

def prompt_topics():
    """Prompt user for topic hashtags"""
    print("\nEnter topics as hashtags (space-separated):")
    print("Example: #array #hash-table #two-pointers")
    topics = input("Topics (press Enter to skip): ").strip()

    if not topics:
        return ""

    # Ensure all topics start with #
    topics_list = topics.split()
    formatted_topics = []
    for topic in topics_list:
        if not topic.startswith('#'):
            formatted_topics.append(f'#{topic}')
        else:
            formatted_topics.append(topic)

    return ' '.join(formatted_topics)

def create_directories(base_path):
    """Create necessary directories"""
    os.makedirs(base_path, exist_ok=True)

def create_solution_header(class_name):
    """Generate solution header file content"""
    return f"""#ifndef {class_name.upper()}_H
#define {class_name.upper()}_H

class Solution {{
public:
    // TODO: Add method signature

private:
    // TODO: Add helper methods if needed
}};

#endif // {class_name.upper()}_H
"""

def create_solution_cpp():
    """Generate solution cpp file content"""
    return f"""#include "solution.h"

// TODO: Implement methods
"""

def create_readme(problem_num, problem_name, difficulty, topics):
    """Generate README content"""
    topics_display = f"\n**Topics**: {topics}" if topics else ""
    return f"""# Problem {problem_num}: {problem_name}

**Difficulty**: {difficulty}{topics_display}

## Description
TODO: Add problem description

## Approach
TODO: Describe your solution approach

## Complexity
- Time: TODO
- Space: TODO

"""

def create_test_file(class_name, snake_name):
    """Generate test file content"""
    return f"""#include <gtest/gtest.h>
#include "problems/{snake_name}/solution.h"

class {class_name}Test : public testing::Test {{
protected:
    Solution solution;
}};

TEST_F({class_name}Test, BasicTest) {{
    // TODO: Write your first test
    EXPECT_TRUE(true);
}}
"""

def update_cmake(test_file_name, source_file_path):
    """Update tests/CMakeLists.txt with test and source files"""
    cmake_path = 'tests/CMakeLists.txt'

    if not os.path.exists(cmake_path):
        print(f"Error: {cmake_path} not found")
        return False

    with open(cmake_path, 'r') as f:
        lines = f.readlines()

    # Find add_executable line
    exe_start = -1
    exe_end = -1
    for i, line in enumerate(lines):
        if 'add_executable(leetcode_tests' in line:
            exe_start = i
        if exe_start != -1 and ')' in line and exe_end == -1:
            exe_end = i
            break

    if exe_start == -1 or exe_end == -1:
        print("Error: Could not find add_executable in CMakeLists.txt")
        return False

    # Check if files already exist
    test_entry = f"    {test_file_name}\n"
    source_entry = f"    ../{source_file_path}\n"

    test_exists = any(test_file_name in line for line in lines[exe_start:exe_end+1])
    source_exists = any(source_file_path in line for line in lines[exe_start:exe_end+1])

    if not test_exists:
        lines.insert(exe_end, test_entry)
        exe_end += 1

    if not source_exists:
        lines.insert(exe_end, source_entry)

    with open(cmake_path, 'w') as f:
        f.writelines(lines)

    return True

def update_root_cmakelists(problem_name):
    """Add solution.cpp to root CMakeLists.txt executable target"""
    cmakelists_path = Path("CMakeLists.txt")

    with open(cmakelists_path, 'r') as f:
        content = f.read()

    solution_file = f"src/problems/{problem_name}/solution.cpp"

    # Check if already added
    if solution_file in content:
        print(f"{solution_file} already in CMakeLists.txt")
        return

    # Pattern for single-line add_executable
    pattern = r"(add_executable\(leetcode\s+src/main\.cpp)(\))"
    replacement = rf"\1\n    {solution_file}\2"

    new_content = re.sub(pattern, replacement, content)

    if new_content == content:
        print(f"Warning: Could not find add_executable(leetcode ...) in CMakeLists.txt")
        return

    with open(cmakelists_path, 'w') as f:
        f.write(new_content)

    print(f"Updated root CMakeLists.txt with {solution_file}")


def update_problem_index(problem_num, problem_name, difficulty, topics):
    """Update docs/PROBLEM_INDEX.md with new problem entry"""
    index_path = 'docs/PROBLEM_INDEX.md'

    if not os.path.exists(index_path):
        print(f"Warning: {index_path} not found, skipping index update")
        return False

    with open(index_path, 'r') as f:
        content = f.read()

    # Find the table and insert new row
    # Look for the header row and insert after it
    table_pattern = r'(\| # \| Problem \| Difficulty \| Topics \| Folder \|\n\|---|---------|------------|--------|--------\|)\n'
    match = re.search(table_pattern, content)

    if not match:
        print("Warning: Could not find table in PROBLEM_INDEX.md")
        return False

    # Create new row
    topics_display = topics if topics else ""
    new_row = f"| {problem_num} | [{problem_name}](../src/problems/{problem_name}/) | {difficulty} | {topics_display} | [Link](../src/problems/{problem_name}/) |\n"

    # Check if entry already exists
    if f"| {problem_num} |" in content:
        print(f"Warning: Problem #{problem_num} already exists in PROBLEM_INDEX.md")
        return False

    # Insert new row after table header
    insert_pos = match.end()
    updated_content = content[:insert_pos] + new_row + content[insert_pos:]

    # Update the timestamp
    today = datetime.now().strftime("%B %d, %Y")
    updated_content = re.sub(
        r'\*Last updated: .*?\*',
        f'*Last updated: {today}*',
        updated_content
    )

    with open(index_path, 'w') as f:
        f.write(updated_content)

    return True

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 new_solution.py <problem_number> <problem_name>")
        print("Example: python3 new_solution.py 1 two-sum")
        sys.exit(1)

    problem_num = sys.argv[1]
    problem_name = sys.argv[2]

    if not validate_inputs(problem_num, problem_name):
        sys.exit(1)

    # Prompt for difficulty and topics
    difficulty = prompt_difficulty()
    topics = prompt_topics()

    class_name = kebab_to_pascal(problem_name)
    snake_name = kebab_to_snake(problem_name)
    problem_dir = f'src/problems/{problem_name}'

    # Create directories
    create_directories(problem_dir)

    # Create solution files
    with open(f'{problem_dir}/solution.h', 'w') as f:
        f.write(create_solution_header(class_name))

    with open(f'{problem_dir}/solution.cpp', 'w') as f:
        f.write(create_solution_cpp())

    with open(f'{problem_dir}/README.md', 'w') as f:
        f.write(create_readme(problem_num, problem_name, difficulty, topics))

    # Create test file
    test_file = f'tests/test_{snake_name}.cpp'
    with open(test_file, 'w') as f:
        f.write(create_test_file(class_name, problem_name))

    # Update CMakeLists.txt
    test_entry = f'test_{snake_name}.cpp'
    source_entry = f'src/problems/{problem_name}/solution.cpp'

    if not update_cmake(test_entry, source_entry):
        sys.exit(1)

    # Update root CMakeLists.txt
    update_root_cmakelists(problem_name)

    # Update PROBLEM_INDEX.md
    update_problem_index(problem_num, problem_name, difficulty, topics)

    print(f"\n✅ Created solution structure for Problem {problem_num}: {problem_name}")
    print(f"   📁 {problem_dir}/")
    print(f"   📄 {test_file}")
    print(f"   📋 Difficulty: {difficulty}")
    if topics:
        print(f"   🏷️  Topics: {topics}")
    print(f"\nNext steps:")
    print(f"  1. Edit {problem_dir}/solution.h and solution.cpp")
    print(f"  2. Write tests in {test_file}")
    print(f"  3. Build: cmake --build build")
    print(f"  4. Test: cd build && ctest --output-on-failure")

if __name__ == '__main__':
    main()

