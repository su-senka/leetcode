#include <gtest/gtest.h>
#include "problems/longest-solution/solution.h"

class LongestSolutionTest : public testing::Test {
protected:
    Solution solution;
};

TEST_F(LongestSolutionTest, BasicTests) {
    EXPECT_EQ(Solution::lengthOfLongestSubstring("abcabcbb"), 3);
    EXPECT_EQ(Solution::lengthOfLongestSubstring("bbbbb"), 1);
    EXPECT_EQ(Solution::lengthOfLongestSubstring("pwwkew"), 3);
    EXPECT_EQ(Solution::lengthOfLongestSubstring(""), 0);
    EXPECT_EQ(Solution::lengthOfLongestSubstring("au"), 2);
    EXPECT_EQ(Solution::lengthOfLongestSubstring("dvdf"), 3);
}
