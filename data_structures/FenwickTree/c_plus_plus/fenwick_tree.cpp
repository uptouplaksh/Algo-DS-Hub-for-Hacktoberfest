#include <iostream>
#include <cassert>
#include "fenwick_tree.h"
using namespace std;

/**
 * Example demonstration in main().
 * Input:
 *   arr = [1, 2, 3, 4, 5]
 *   Then perform:
 *     1) Query sum [1, 3]
 *     2) Add +2 at index 2
 *     3) Query sum [1, 3] again
 */
int main() {
    BIT<long long> bit(5);

    // Initialize array [1, 2, 3, 4, 5]
    for (int i = 0; i < 5; i++)
        bit.set(i, i + 1);

    cout << "Initial array: [1, 2, 3, 4, 5]\n";

    // Query 1: sum of [1, 3] (2 + 3 + 4 = 9)
    cout << "Sum [1, 3] = " << bit.range_sum(1, 3) << "\n";

    // Update: add +2 at index 2 → arr[2] = 5 now
    bit.add(2, 2);
    cout << "Added +2 to index 2.\n";

    // Query 2: sum of [1, 3] again (2 + 5 + 4 = 11)
    cout << "Sum [1, 3] after update = " << bit.range_sum(1, 3) << "\n";

    // Verify correctness with assertion
    assert(bit.range_sum(0, 4) == 1 + 2 + 5 + 4 + 5);

    cout << "All operations completed successfully.\n";
}
/*
Example Output:
Initial array: [1, 2, 3, 4, 5]
Sum [1, 3] = 9
Added +2 to index 2.
Sum [1, 3] after update = 11
All operations completed successfully.
*/
