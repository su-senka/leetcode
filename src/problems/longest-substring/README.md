# Problem 3: longest-substring

**Difficulty**: Medium
**Topics**: #string #sliding-window #hash-table

## Description
Given a string `s`, find the length of the longest substring without repeating characters.

## Approach
Maintain a sliding window `[left, right]` with all unique chars.  
For each `right`, if `s[right]` appeared inside the window, move `left` to `last[s[right]] + 1`.  
Update `last` and track the best window length.

**Notes:** This version assumes ASCII via a 256-sized table. For full Unicode, decode to code points and use `unordered_map<char32_t, int>`.

## Complexity
- Time: O(n) — each index moves forward at most once
- Space: O(min(n, σ)) — last-seen positions for the alphabet

