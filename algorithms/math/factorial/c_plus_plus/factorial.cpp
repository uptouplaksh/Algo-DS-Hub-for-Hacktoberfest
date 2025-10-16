/*
Factorial Calculation using Recursion in C++

Time Complexity: O(n)   -> The function calls itself n times.
Space Complexity: O(n)  -> Due to recursive call stack.

Explanation:
- Base Case: If n is 0 or 1, return 1.
- Recursive Step: n! = n * factorial(n - 1)

Edge Cases:
- Negative numbers: Factorial is not defined.
- Large n (>20): May overflow 64-bit integer.
*/

#include <iostream>
using namespace std;

// Recursive function to calculate factorial
unsigned long long factorial(int n) {
    // Base Case
    if (n <= 1) return 1;

    // Recursive Step
    return n * factorial(n - 1);
}

int main() {
    int n;
    cout << "Enter a non-negative integer: ";
    cin >> n;

    // Handle invalid input or negative numbers
    if (cin.fail() || n < 0) {
        cout << "Invalid input! Please enter a non-negative integer." << endl;
        return 1;
    }

    // Warn if factorial might overflow
    if (n > 20) {
        cout << "Warning: Factorial may overflow for n > 20." << endl;
    }

    cout << "Factorial of " << n << " is: " << factorial(n) << endl;

    // Example demonstration
    cout << "\nExample:\n";
    cout << n << "! = ";
    for (int i = n; i >= 1; i--) {
        cout << i;
        if (i > 1) cout << " × ";
    }
    cout << " = " << factorial(n) << endl;

        return 0;
    }

