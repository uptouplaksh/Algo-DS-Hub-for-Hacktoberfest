/*
--------------------------------------------------------
    Time and Space Complexity
--------------------------------------------------------

    Let:
        n = number of elements
        k = maximum number of digits in the largest number

    - Counting Sort (per digit): O(n + 10) ≈ O(n)
    - Radix Sort overall: O(k * n)

    For decimal integers, k is small (log10(max)), 
    making Radix Sort nearly linear for practical use.

    Space Complexity: O(n + 10) ≈ O(n)
--------------------------------------------------------
*/
#include "radix_sort.h"
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
--------------------------------------------------------
    Radix Sort Algorithm (Base 10 Implementation)
--------------------------------------------------------

    Concept:
    - Radix Sort works by sorting numbers digit by digit,
      starting from the least significant digit (LSD)
      to the most significant digit (MSD).

    - It uses a stable sorting algorithm (like Counting Sort)
      as a subroutine to sort numbers based on individual digits.
*/

// Function to get the maximum element in the array
int getMax(const vector<int>& arr) {
    int mx = arr[0];
    for (int num : arr)
        if (num > mx)
            mx = num;
    return mx;
}

// Counting sort that sorts arr[] according to the digit represented by exp
void countingSort(vector<int>& arr, int exp) {
    int n = arr.size();
    vector<int> output(n);  // Output array
    int count[10] = {0};    // Count array for digits (0-9)

    // Count occurrences of each digit in the current place value
    for (int i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;

    // Change count[i] so that count[i] now contains the actual
    // position of this digit in output[]
    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];

    // Build the output array (stable sorting: iterate from the end)
    for (int i = n - 1; i >= 0; i--) {
        int digit = (arr[i] / exp) % 10;
        output[count[digit] - 1] = arr[i];
        count[digit]--;
    }

    // Copy the output array to arr[]
    for (int i = 0; i < n; i++)
        arr[i] = output[i];
}

// Main Radix Sort function
void radixSort(vector<int>& arr) {
    // If array is empty, no need to sort
    if (arr.empty()) {
        return;
    }

    // Find the maximum number to know the number of digits
    int m = getMax(arr);

    // Apply counting sort to sort elements based on every digit
    // exp is 10^i where i is the current digit number
    for (int exp = 1; m / exp > 0; exp *= 10)
        countingSort(arr, exp);
}
