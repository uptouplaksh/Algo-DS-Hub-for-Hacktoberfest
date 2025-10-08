/**
 * Fibonacci Sequence - Recursive Implementation in JavaScript
 * 
 * Description:
 * This module demonstrates a simple recursive approach to generate 
 * the nth number in the Fibonacci Sequence.
 * 
 * Fibonacci Rule:
 * F(0) = 0
 * F(1) = 1
 * F(n) = F(n-1) + F(n-2)
 * 
 * Note:
 * This is the naive recursive method — highly inefficient for large n 
 * because it recomputes results multiple times.
 * 
 * Time Complexity: O(2^n)
 * Space Complexity: O(n)  (due to recursive call stack)
 */

function fibonacciRecursive(n) {
  // Base cases
  if (n === 0) return 0;
  if (n === 1) return 1;

  // Recursive case: Sum of two previous Fibonacci numbers
  return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// ------------------------- RUNNABLE EXAMPLE -------------------------
if (require.main === module) {
  console.log("Fibonacci Sequence using Recursion\n");

  const n = 7; // Example: Find the 7th Fibonacci number
  console.log(`n = ${n}`);
  console.log(`Fibonacci(${n}) = ${fibonacciRecursive(n)}\n`);

  console.log("Note: This approach becomes very slow for large n due to exponential time complexity.");
}
