

def product_except_self(nums):
    """
    Given an array of integers, returns an array such that the output at index i 
    is the product of all the elements of the original array except the one at i. 
    The solution should not use the division operator.

    # Time Complexity: O(n) - We traverse the array a constant number of times.
    # Space Complexity: O(1) - We use the output array for storage, not counting the input and output space.

    Args:
        nums (List[int]): Input list of integers.

    Returns:
        List[int]: List where each element is the product of all other elements.
    """

    n=len(nums) # Length of the input array
    result=[1]*n # Initialize the result array with 1's

    # Calculate left products
    for i in range(1,n): # Start from index 1 to n-1
        result[i]=result[i-1]*nums[i-1] # At index i, product of all elements to the left of i 
    
    # Calculate right products and final result
    right_product=1 # Initialize right product
    for i in range(n-1,-1,-1): # Traverse from the end to the start
        result[i]*=right_product # Multiply with the product of all elements to the right of i
        right_product*=nums[i] # Update right product

    return result # Return the final result array

# Example usage
if __name__ == "__main__": # This block will only run if the script is executed directly
    nums=[1,2,3,4] # Example input
    print("Input array:", nums) # Print the input array

    print("Product Except Self:",product_except_self(nums)) # Print the result  

