#include <gtest/gtest.h>
#include "problems/add-two-numbers/solution.h"

class AddTwoNumbersTest : public testing::Test {
protected:
    Solution solution;
};

TEST_F(AddTwoNumbersTest, BasicTests) {
    // Test case 1: (2 -> 4 -> 3) + (5 -> 6 -> 4) = (7 -> 0 -> 8)
    auto* l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
    auto* l2 = new ListNode(5, new ListNode(6, new ListNode(4)));
    const auto result = Solution::addTwoNumbers(l1, l2);
    EXPECT_EQ(result->val, 7);
    EXPECT_EQ(result->next->val, 0);
    EXPECT_EQ(result->next->next->val, 8);

    // Clean up memory
    delete result->next->next;
    delete result->next;
    delete result;
}
