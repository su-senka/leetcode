# Google Test configuration for LeetCode solutions

# Test executable - will add individual test sources as we create solutions
add_executable(leetcode_tests
    test_template.cpp
        ../src/problems/two-sum/solution.cpp
    test_two_sum.cpp
    test_add_two_numbers.cpp
    ../src/problems/add-two-numbers/solution.cpp
    test_longest_solution.cpp
    ../src/problems/longest-solution/solution.cpp
    test_median_of_two_sorted_arrays.cpp
    ../src/problems/median-of-two-sorted-arrays/solution.cpp
    test_longest_palindromic_substring.cpp
    ../src/problems/longest-palindromic-substring/solution.cpp
)

# Link Google Test
target_link_libraries(leetcode_tests
    GTest::gtest_main
    GTest::gtest
)

# Include directories
target_include_directories(leetcode_tests PRIVATE
    ${CMAKE_SOURCE_DIR}/src
    ${CMAKE_SOURCE_DIR}/src/problems
)

# Discover tests
include(GoogleTest)
gtest_discover_tests(leetcode_tests)

# Individual test files will be added here as problems are created

