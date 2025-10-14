#include <iostream>
#include <cassert>
#include <string>
#include "fenwick_tree.h"
using namespace std;

/*
    Unit Tests for Fenwick Tree (Binary Indexed Tree)
    
    This file contains comprehensive tests to verify:
    - query() for prefix sums
    - rangeQuery() for various ranges
    - update() functionality and re-testing after updates
    
    Compile and run:
    g++ -std=c++17 test_fenwick_tree.cpp -o test_fenwick_tree
    ./test_fenwick_tree
*/

// Wrapper class to provide 1-based indexing interface for tests
// while using the 0-based BIT class from fenwick_tree.h
class FenwickTree 
{
    BIT<int> bit;
    
public:
    explicit FenwickTree(int n) : bit(n) {}

    void update(int i, int delta) 
    {
        bit.add(i - 1, delta); // Convert 1-based to 0-based
    }
    
    int query(int i) const 
    {
        return bit.pref_sum(i - 1); // Convert 1-based to 0-based
    }
    
    int rangeQuery(int l, int r) const 
    {
        return bit.range_sum(l - 1, r - 1); // Convert 1-based to 0-based
    }
};

// Test counter
int tests_passed = 0;
int tests_failed = 0;

// Helper function to run a test
void test_assert(bool condition, const string& test_name) 
{
    if (condition) {
        cout << "✅ PASS: " << test_name << endl;
        tests_passed++;
    } else {
        cout << "❌ FAIL: " << test_name << endl;
        tests_failed++;
    }
}

// Test 1: Test prefix sum queries
void test_prefix_sum_queries() 
{
    cout << "\n━━━ Test 1: Prefix Sum Queries ━━━" << endl;
    
    FenwickTree ft(10);
    vector<int> arr = {0, 3, 2, -1, 6, 5, 4, -3, 3, 7, 2};
    
    // Build the tree
    for(int i = 1; i <= 10; ++i) {
        ft.update(i, arr[i]);
    }
    
    // Test prefix sums
    test_assert(ft.query(1) == 3, "Prefix sum up to index 1");
    test_assert(ft.query(2) == 5, "Prefix sum up to index 2 (3+2)");
    test_assert(ft.query(3) == 4, "Prefix sum up to index 3 (3+2-1)");
    test_assert(ft.query(5) == 15, "Prefix sum up to index 5 (3+2-1+6+5)");
    test_assert(ft.query(10) == 28, "Prefix sum up to index 10 (all elements)");
}

// Test 2: Test range queries for various ranges
void test_range_queries() 
{
    cout << "\n━━━ Test 2: Range Queries ━━━" << endl;
    
    FenwickTree ft(10);
    vector<int> arr = {0, 3, 2, -1, 6, 5, 4, -3, 3, 7, 2};
    
    for(int i = 1; i <= 10; ++i) {
        ft.update(i, arr[i]);
    }
    
    // Test various range queries
    test_assert(ft.rangeQuery(1, 1) == 3, "Range [1,1] = 3");
    test_assert(ft.rangeQuery(1, 5) == 15, "Range [1,5] = 15");
    test_assert(ft.rangeQuery(3, 8) == 14, "Range [3,8] = -1+6+5+4-3+3");
    test_assert(ft.rangeQuery(5, 7) == 6, "Range [5,7] = 5+4-3");
    test_assert(ft.rangeQuery(1, 10) == 28, "Range [1,10] = all elements");
    test_assert(ft.rangeQuery(6, 10) == 13, "Range [6,10] = 4-3+3+7+2");
}

// Test 3: Test updates and re-query
void test_updates_and_requery() 
{
    cout << "\n━━━ Test 3: Updates and Re-Query ━━━" << endl;
    
    FenwickTree ft(10);
    vector<int> arr = {0, 3, 2, -1, 6, 5, 4, -3, 3, 7, 2};
    
    for(int i = 1; i <= 10; ++i) {
        ft.update(i, arr[i]);
    }
    
    // Initial query
    test_assert(ft.query(5) == 15, "Initial prefix sum up to index 5");
    
    // Update index 4: add +5 (6 -> 11)
    ft.update(4, 5);
    test_assert(ft.query(5) == 20, "After update(4, +5), prefix sum up to 5");
    test_assert(ft.rangeQuery(3, 8) == 19, "After update, range [3,8]");
    
    // Update index 1: add -2 (3 -> 1)
    ft.update(1, -2);
    test_assert(ft.query(1) == 1, "After update(1, -2), prefix sum up to 1");
    test_assert(ft.query(5) == 18, "After second update, prefix sum up to 5");
    
    // Update index 10: add +10 (2 -> 12)
    ft.update(10, 10);
    test_assert(ft.query(10) == 41, "After update(10, +10), prefix sum up to 10");
    test_assert(ft.rangeQuery(8, 10) == 22, "After update, range [8,10]");
}

// Test 4: Edge cases
void test_edge_cases() 
{
    cout << "\n━━━ Test 4: Edge Cases ━━━" << endl;
    
    // Test with single element
    FenwickTree ft1(1);
    ft1.update(1, 5);
    test_assert(ft1.query(1) == 5, "Single element tree");
    test_assert(ft1.rangeQuery(1, 1) == 5, "Single element range query");
    
    // Test with all zeros
    FenwickTree ft2(5);
    test_assert(ft2.query(5) == 0, "All zeros - prefix sum");
    test_assert(ft2.rangeQuery(1, 5) == 0, "All zeros - range query");
    
    // Test with negative numbers
    FenwickTree ft3(5);
    ft3.update(1, -5);
    ft3.update(2, -3);
    ft3.update(3, -1);
    test_assert(ft3.query(3) == -9, "Negative numbers - prefix sum");
    test_assert(ft3.rangeQuery(1, 3) == -9, "Negative numbers - range query");
}

// Test 5: Multiple updates on same index
void test_multiple_updates() 
{
    cout << "\n━━━ Test 5: Multiple Updates on Same Index ━━━" << endl;
    
    FenwickTree ft(5);
    vector<int> arr = {0, 1, 2, 3, 4, 5};
    
    for(int i = 1; i <= 5; ++i) {
        ft.update(i, arr[i]);
    }
    
    // Initial state
    test_assert(ft.query(3) == 6, "Initial: prefix sum up to 3 = 1+2+3");
    
    // Multiple updates on index 2
    ft.update(2, 5);  // 2 -> 7
    test_assert(ft.query(3) == 11, "After first update on index 2");
    
    ft.update(2, -3); // 7 -> 4
    test_assert(ft.query(3) == 8, "After second update on index 2");
    
    ft.update(2, 10); // 4 -> 14
    test_assert(ft.query(3) == 18, "After third update on index 2");
}

// Test 6: Large range queries
void test_large_range() 
{
    cout << "\n━━━ Test 6: Large Range Operations ━━━" << endl;
    
    FenwickTree ft(100);
    
    // Initialize with values 1, 2, 3, ..., 100
    for(int i = 1; i <= 100; ++i) {
        ft.update(i, i);
    }
    
    // Sum of 1 to 100 = 100 * 101 / 2 = 5050
    test_assert(ft.query(100) == 5050, "Sum of 1 to 100");
    
    // Range [50, 100]: sum of 50 to 100
    // = (100*101/2) - (49*50/2) = 5050 - 1225 = 3825
    test_assert(ft.rangeQuery(50, 100) == 3825, "Range [50,100]");
    
    // Range [1, 50]
    test_assert(ft.rangeQuery(1, 50) == 1275, "Range [1,50]");
}

int main() 
{
    cout << "╔════════════════════════════════════════════════════════════════╗" << endl;
    cout << "║          FENWICK TREE UNIT TESTS                               ║" << endl;
    cout << "╚════════════════════════════════════════════════════════════════╝" << endl;
    
    // Run all test suites
    test_prefix_sum_queries();
    test_range_queries();
    test_updates_and_requery();
    test_edge_cases();
    test_multiple_updates();
    test_large_range();
    
    // Print summary
    cout << "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" << endl;
    cout << "RESULTS: " << tests_passed << "/" << (tests_passed + tests_failed) 
         << " tests PASSED" << endl;
    cout << "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" << endl;
    
    if (tests_failed == 0) {
        cout << "✅ All tests PASSED!" << endl;
        return 0;
    } else {
        cout << "❌ " << tests_failed << " test(s) FAILED!" << endl;
        return 1;
    }
}
