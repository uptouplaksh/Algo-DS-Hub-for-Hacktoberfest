#ifndef FENWICK_TREE_H
#define FENWICK_TREE_H

#include <vector>
using namespace std;

/**
 * ------------------------------------------
 * Binary Indexed Tree (Fenwick Tree)
 * ------------------------------------------
 * Supports:
 *  - Point updates: Add value to an element
 *  - Range sum queries: Sum over [l, r]
 *
 * Time Complexity:
 *  - Update (add/set): O(log n)
 *  - Prefix sum query: O(log n)
 *  - Range sum query: O(log n)
 *
 * Space Complexity:
 *  - O(n)
 *
 * Example use:
 *  BIT<long long> bit(5);
 *  bit.set(0, 5);  // arr[0] = 5
 *  bit.add(3, 2);  // arr[3] += 2
 *  cout << bit.pref_sum(3); // prefix sum [0..3]
 * ------------------------------------------
 */

template <class T>
class BIT {
private:
    int size;
    vector<T> bit; // BIT array (1-indexed)
    vector<T> arr; // Original array (0-indexed)

public:
    // Constructor: initialize arrays of given size
    BIT(int n) : size(n), bit(n + 1, 0), arr(n, 0) {}

    /** Sets the value at index ind (0-indexed) to val. */
    void set(int ind, T val) {
        add(ind, val - arr[ind]);  // find difference and update
    }

    /** Adds val to the element at index ind (0-indexed). */
    void add(int ind, T val) {
        arr[ind] += val;
        ind++; // BIT uses 1-based indexing
        for (; ind <= size; ind += ind & -ind)
            bit[ind] += val;
    }

    /** @return The prefix sum over [0, ind] (0-indexed). */
    T pref_sum(int ind) const {
        if (ind < 0) return 0; // handle invalid index
        ind++;
        T total = 0;
        for (; ind > 0; ind -= ind & -ind)
            total += bit[ind];
        return total;
    }

    /** @return The sum of all values in [l, r] inclusive. */
    T range_sum(int l, int r) const {
        return pref_sum(r) - pref_sum(l - 1);
    }
};

#endif // FENWICK_TREE_H
