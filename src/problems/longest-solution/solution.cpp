#include "solution.h"
#include <vector>
#include <algorithm>

int Solution::lengthOfLongestSubstring(const std::string& s) {
    std::vector last(256, -1);
    int best = 0;
    int left = 0;
    for (int right = 0; right < static_cast<int>(s.size()); ++right) {
        const auto c = static_cast<unsigned char>(s[right]);
        if (last[c] >= left) left = last[c] + 1;
        last[c] = right;
        best = std::max(best, right - left + 1);
    }
    return best;
}
