#include <iostream>
#include <vector>

#include "problems/two-sum/solution.h"

using namespace std;

void printHeader(const string& problemName) {
    cout << "\n=== " << problemName << " ===" << endl;
}

int main() {
    cout << "LeetCode Solutions Demo" << endl;
    cout << "======================" << endl;

    printHeader("Two Sum (LeetCode #1)");

    const vector nums = {2, 7, 11, 15};
    constexpr int target = 9;
    const auto result = Solution::twoSum(nums, target);

    cout << "Input: [2, 7, 11, 15], target = 9" << endl;
    cout << "Output: [" << result[0] << ", " << result[1] << "]" << endl;

    return 0;
}
