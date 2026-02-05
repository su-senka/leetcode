#include "solution.h"
#include <vector>
#include <algorithm>

using namespace std;

int Solution::lengthOfLongestSubstring(const string& s) {
    // For ASCII last index of each char, -1 means unseen.
    vector<int> last(256, -1);

    int best = 0;
    int left = 0;

    for (int right = 0; right < (int)s.size(); ++right) {
        unsigned char c = static_cast<unsigned char>(s[right]);
        if (last[c] >= left) {
            left = last[c] + 1;      // jump left past the duplicate
        }
        last[c] = right;
        best = max(best, right - left + 1);
    }
    return best;
}
