# Problem 1: two-sum

**Difficulty**: Easy
**Topics**: #array #hash-table

## Description

Given an array `nums` and an integer `target`, return the indices of the two numbers that add up to `target`.  
Exactly one valid pair is guaranteed to exist.

## Approach

We scan the array once while keeping a hash map `value → index` of numbers we’ve already seen.

For each number `x`:
1. Compute `need = target - x`.
2. If `need` is already in the map, return its stored index and the current index.
3. Otherwise, store `x` and its index in the map.

This way we find the pair as soon as the second number appears.

## Complexity
- Time: `O(n)` — we inspect each element once, which is optimal because every element must be checked.
- Space: `O(n)` — worst case we store every number in the map.

## Solution
See `solution.h` and `solution.cpp`
