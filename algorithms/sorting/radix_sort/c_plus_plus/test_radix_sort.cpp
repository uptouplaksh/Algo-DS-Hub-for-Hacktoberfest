#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

#include "radix_sort.h"

// Test function to print and verify the sorted array
void run_test(std::vector<int>& test_case, const std::vector<int>& expected) {
    radixSort(test_case);
    assert(test_case == expected);
}

int main() {
    // Test Case 1: Standard unsorted list
    std::vector<int> test1 = {170, 45, 75, 90, 802, 24, 2, 66};
    std::vector<int> expected1 = {2, 24, 45, 66, 75, 90, 170, 802};
    run_test(test1, expected1);
    std::cout << "Test Case 1 (Standard Unsorted) Passed!" << std::endl;

    // Test Case 2: List with varying number of digits
    std::vector<int> test2 = {1, 100, 10};
    std::vector<int> expected2 = {1, 10, 100};
    run_test(test2, expected2);
    std::cout << "Test Case 2 (Varying Digits) Passed!" << std::endl;

    // Test Case 3: Already sorted list
    std::vector<int> test3 = {10, 20, 30, 40, 50};
    std::vector<int> expected3 = {10, 20, 30, 40, 50};
    run_test(test3, expected3);
    std::cout << "Test Case 3 (Already Sorted) Passed!" << std::endl;

    // Test Case 4: Empty list
    std::vector<int> test4 = {};
    std::vector<int> expected4 = {};
    radixSort(test4);
    assert(test4 == expected4);
    std::cout << "Test Case 4 (Empty List) Passed!" << std::endl;

    // Test Case 5: Single-element list
    std::vector<int> test5 = {42};
    std::vector<int> expected5 = {42};
    radixSort(test5);
    assert(test5 == expected5);
    std::cout << "Test Case 5 (Single Element) Passed!" << std::endl;
    
    // Test Case 6: List with duplicate values
    std::vector<int> test6 = {170, 45, 75, 90, 802, 24, 2, 66, 45};
    std::vector<int> expected6 = {2, 24, 45, 45, 66, 75, 90, 170, 802};
    run_test(test6, expected6);
    std::cout << "Test Case 6 (With Duplicates) Passed!" << std::endl;

    std::cout << "\nAll Radix Sort test cases passed!" << std::endl;

    return 0;
}