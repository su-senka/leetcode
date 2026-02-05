#ifndef ADDTWONUMBERS_H
#define ADDTWONUMBERS_H

struct ListNode {
    int val;
    ListNode* next;
    explicit ListNode(const int x) : val(x), next(nullptr) {}
    ListNode(const int x, ListNode* n) : val(x), next(n) {}  // Add this
};


class Solution {
public:
    static ListNode* addTwoNumbers(ListNode* l1, ListNode* l2);
};

#endif // ADDTWONUMBERS_H
