#include "problems/two-sum/solution.h"
#include <unordered_map>

std::vector<int> Solution::twoSum(const std::vector<int>& nums, const int target) {
    std::unordered_map<int, int> idx; // value -> index

    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        int need = target - nums[i];
        if (auto it = idx.find(need); it != idx.end())
            return {it->second, i};
        idx[nums[i]] = i;
    }

    return {};
}
