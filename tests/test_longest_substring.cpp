#include <gtest/gtest.h>
#include "problems/longest-substring/solution.h"

class LongestSubstringTest : public testing::Test {
protected:
    Solution solution;
};

TEST_F(LongestSubstringTest, ExampleOne) {
    EXPECT_EQ(solution.lengthOfLongestSubstring("abcabcbb"), 3);
}

TEST_F(LongestSubstringTest, ExampleTwo) {
    EXPECT_EQ(solution.lengthOfLongestSubstring("bbbbb"), 1);
}

TEST_F(LongestSubstringTest, ExampleThree) {
    EXPECT_EQ(solution.lengthOfLongestSubstring("pwwkew"), 3);
}

TEST_F(LongestSubstringTest, EmptyString) {
    EXPECT_EQ(solution.lengthOfLongestSubstring(""), 0);
}

TEST_F(LongestSubstringTest, SingleCharacter) {
    EXPECT_EQ(solution.lengthOfLongestSubstring("a"), 1);
}

TEST_F(LongestSubstringTest, AllUnique) {
    EXPECT_EQ(solution.lengthOfLongestSubstring("abcdef"), 6);
}
