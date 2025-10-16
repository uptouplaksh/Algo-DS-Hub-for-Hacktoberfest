# sieve.py
"""
Sieve of Eratosthenes Algorithm to find all prime numbers up to a given number n.
This algorithm marks non-prime numbers (composites) as False in a boolean list
and leaves primes as True.

Time Complexity:
- The time complexity of the Sieve of Eratosthenes is O(n log log n), 
  where n is the input number up to which we want to find primes.

Space Complexity:
- The space complexity is O(n), since we need an array of size n+1 to store boolean values.
"""

def sieve_of_eratosthenes(n):
    """
    Returns a list of all prime numbers up to n (inclusive).
    
    Args:
    n (int): The upper bound of numbers to check for primality.
    
    Returns:
    List[int]: A list containing all primes less than or equal to n.
    """
    # Step 1: Initialize a boolean list of size n+1 with True values
    # True means the number is prime, False means the number is composite.
    sieve = [True] * (n + 1)
    
    # Step 2: Set the first two numbers (0 and 1) as not prime
    sieve[0], sieve[1] = False, False
    
    # Step 3: Start marking the multiples of each prime starting from 2
    for current in range(2, int(n ** 0.5) + 1):
        if sieve[current]:
            # Mark multiples of the current prime as False
            for multiple in range(current * current, n + 1, current):
                sieve[multiple] = False
    
    # Step 4: Extract all the prime numbers from the sieve
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    
    return primes

# Example usage:
if __name__ == "__main__":
    n = 30  # You can change this value to test with other numbers
    print(f"Prime numbers up to {n}: {sieve_of_eratosthenes(n)}")
