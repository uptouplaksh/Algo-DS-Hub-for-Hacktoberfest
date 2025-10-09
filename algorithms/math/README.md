# Mathematical Algorithms

This directory contains implementations of fundamental mathematical algorithms and computational techniques in various programming languages.

## Overview

Mathematical algorithms form the foundation of computer science and are used across diverse domains including cryptography, scientific computing, computer graphics, and data analysis.

## Implemented Algorithms

### 1. Factorial
**Directory:** `factorial/`

The factorial of a non-negative integer n (denoted as n!) is the product of all positive integers less than or equal to n.

**Formula:** `n! = n × (n-1) × (n-2) × ... × 2 × 1`

**Implementations:**
- **Python** (`factorial/python/factorial.py`)
- **C++** (`factorial/c_plus_plus/factorial.cpp`)

**Properties:**
- Time Complexity: O(n)
- Space Complexity: O(1) iterative, O(n) recursive
- Base case: 0! = 1

**Use Cases:**
- Combinatorics and permutations
- Probability calculations
- Series expansions

---

### 2. Fibonacci Sequence
**Directory:** `fibonacci/`

A sequence where each number is the sum of the two preceding ones, starting from 0 and 1.

**Formula:** `F(n) = F(n-1) + F(n-2)`, where `F(0) = 0, F(1) = 1`

**Implementations:**
- **Python** (`fibonacci/python/fibonacci_iterative.py`) - Iterative approach
- **JavaScript** (`fibonacci/javascript/FibonacciRecursive.js`) - Recursive approach

**Properties:**
- Iterative: Time O(n), Space O(1)
- Recursive: Time O(2^n), Space O(n)
- Dynamic Programming: Time O(n), Space O(n)

**Use Cases:**
- Algorithm analysis
- Natural patterns modeling
- Financial modeling

---

### 3. Greatest Common Divisor (GCD)
**Directory:** `gcd/`

The largest positive integer that divides each of the given integers without a remainder.

**Algorithm:** Euclidean algorithm - one of the oldest algorithms still in common use.

**Implementations:**
- **C++** (`gcd/c_plus_plus/gcd.cpp`)

**Properties:**
- Time Complexity: O(log(min(a,b)))
- Space Complexity: O(1)

**Use Cases:**
- Fraction simplification
- Cryptography (RSA algorithm)
- Number theory problems

---

## How to Contribute

We welcome contributions of new mathematical algorithms or implementations in different languages!

### Suggested Algorithms to Add:
- Prime number checkers (Sieve of Eratosthenes)
- Least Common Multiple (LCM)
- Power calculation (fast exponentiation)
- Square root algorithms (Newton's method)
- Matrix operations (multiplication, determinant)
- Euclidean distance
- Modular arithmetic operations
- Number base conversions
- Binomial coefficients
- Catalan numbers

### Contribution Guidelines:
1. Create a new directory for your algorithm
2. Organize by programming language
3. Include mathematical formula in comments
4. Add complexity analysis
5. Provide example usage
6. Follow the existing project structure

## Language Support

Current implementations are available in:
- Python
- C++
- JavaScript

We encourage implementations in other languages like Java, Go, Rust, C, etc.

## Resources

- [Mathematical Algorithms - GeeksforGeeks](https://www.geeksforgeeks.org/mathematical-algorithms/)
- [Number Theory Algorithms](https://cp-algorithms.com/)
- [Introduction to Algorithms - CLRS](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)
