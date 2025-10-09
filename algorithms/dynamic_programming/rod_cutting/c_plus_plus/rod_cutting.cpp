/*
rod_cutting.cpp

This program solves the Rod Cutting Problem using Dynamic Programming.

Given a rod of length n and an array of prices for each length, 
the goal is to determine the maximum value obtainable by cutting 
the rod and selling the pieces.

Time Complexity: O(n^2)
Space Complexity: O(n)
*/

#include <iostream>
#include <vector>
#include <algorithm> // for max

using namespace std;

// Function to solve the Rod Cutting Problem
int rodCutting(const vector<int>& prices, int n) {
    vector<int> dp(n + 1, 0); // dp[i] stores max value for rod of length i

    // Build the table dp[] in bottom-up manner
    for (int i = 1; i <= n; ++i) {
        int max_val = 0;
        for (int j = 0; j < i; ++j) {
            max_val = max(max_val, prices[j] + dp[i - j - 1]);
        }
        dp[i] = max_val;
    }

    return dp[n];
}

// Example usage
int main() {
    vector<int> prices = {1, 5, 8, 9, 10, 17, 17, 20}; // prices for rod lengths 1..8
    int n = prices.size();

    cout << "Rod length: " << n << endl;
    cout << "Prices: ";
    for (int price : prices) cout << price << " ";
    cout << endl;

    int max_value = rodCutting(prices, n);
    cout << "Maximum obtainable value: " << max_value << endl;

    return 0;
}