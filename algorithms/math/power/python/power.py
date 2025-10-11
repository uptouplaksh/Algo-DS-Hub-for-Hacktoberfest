# File: algorithms/math/power/python/power.py

def power(x, n):
    """
    Calculate x raised to the power of n using recursion and exponentiation by squaring.
    
    Args:
        x (float): The base number.
        n (int): The exponent to which the base is raised.
        
    Returns:
        float: The result of x raised to the power of n.
        
    Time Complexity:
        - O(log n): The function reduces the problem size by half with each recursive call, 
          leading to a logarithmic time complexity in terms of the exponent.

    Space Complexity:
        - O(log n): Recursion depth is proportional to the logarithm of n.

    Explanation:
        - If n is even, x^n can be reduced to (x^(n/2))^2.
        - If n is odd, x^n can be reduced to x * (x^((n-1)/2))^2.
    """
    # Base case: x^0 = 1
    if n == 0:
        return 1
    
    # Handle negative exponents
    elif n < 0:
        x = 1 / x
        n = -n
    
    # Recursively calculate power using exponentiation by squaring
    if n % 2 == 0:  # If n is even
        half_power = power(x, n // 2)
        return half_power * half_power
    else:  # If n is odd
        half_power = power(x, (n - 1) // 2)
        return x * half_power * half_power

# Example usage
if __name__ == "__main__":
    base = 2
    exponent = 10
    result = power(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}")
