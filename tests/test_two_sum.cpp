#include <gtest/gtest.h>
#include "two-sum/solution.h"

class TwoSumTest : public testing::Test {
protected:
    Solution solution;
};

TEST_F(TwoSumTest, BasicTests) {
    const std::vector nums1 = {2, 7, 11, 15};
    constexpr int target1 = 9;
    const std::vector<int> result1 = Solution::twoSum(nums1, target1);
    EXPECT_EQ(result1, (std::vector{0, 1}));

    const std::vector nums2 = {3, 2, 4};
    constexpr int target2 = 6;
    const std::vector<int> result2 = Solution::twoSum(nums2, target2);
    EXPECT_EQ(result2, (std::vector{1, 2}));

    const std::vector nums3 = {3, 3};
    constexpr int target3 = 6;
    const std::vector<int> result3 = Solution::twoSum(nums3, target3);
    EXPECT_EQ(result3, (std::vector{0, 1}));
}