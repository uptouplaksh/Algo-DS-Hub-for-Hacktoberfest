# This module implements a solution for the Best Time to Buy and Sell Stock problem.

from typing import List

def max_profit(prices: List[int]) -> int:
    """
    Calculates the maximum profit that can be achieved by buying a stock on one
    day and selling it on a future day.

    The function iterates through the list of stock prices, keeping track of the
    minimum price seen so far (the best day to buy) and the maximum profit
    that can be achieved.

    Complexity Analysis:
    - Time Complexity: O(n), where n is the number of days (the length of the
      prices list). We iterate through the list only once.
    - Space Complexity: O(1), as we only use a constant amount of extra
      space for variables (min_price, max_profit).

    Args:
        prices: A list of integers where prices[i] is the price of a given
                stock on the ith day.

    Returns:
        The maximum profit possible. If no profit can be made (prices are
        always decreasing), it returns 0.
    """
    # Initialize min_price to a very large value (infinity) to ensure the
    # price on the first day is picked as the initial minimum.
    
    min_price = float('inf')
    
    # Initialize max_profit to 0, as profit cannot be negative. If we can't
    # make a profit, we make 0 profit.
    
    max_profit_val = 0

    # Iterate through each price in the list of prices.
    
    for price in prices:
        
        # If the current price is lower than the minimum price seen so far,
        # update the minimum price. This is a potential new best day to buy.
        
        if price < min_price:
            min_price = price
            
        # Calculate the potential profit if we were to sell at the current price
        # having bought at the lowest price seen before.
        
        elif price - min_price > max_profit_val:
            # If this potential profit is greater than our recorded max profit,
            # update the max profit.
            
            max_profit_val = price - min_price

    return max_profit_val

# Runnable Example Block
if __name__ == '__main__':
    
    # Example 1: Prices where profit can be made
    
    stock_prices_1 = [7, 1, 5, 3, 6, 4]
    profit_1 = max_profit(stock_prices_1)
    print(f"Stock Prices: {stock_prices_1}")
    print(f"Maximum Profit: {profit_1}")  # Expected output: 5 (buy at 1, sell at 6)
    print("-" * 20)

    # Example 2: Prices are continuously decreasing, no profit possible
    
    stock_prices_2 = [7, 6, 4, 3, 1]
    profit_2 = max_profit(stock_prices_2)
    print(f"Stock Prices: {stock_prices_2}")
    print(f"Maximum Profit: {profit_2}")  # Expected output: 0
    print("-" * 20)

    # Example 3: Empty list
    
    stock_prices_3 = []
    profit_3 = max_profit(stock_prices_3)
    print(f"Stock Prices: {stock_prices_3}")
    print(f"Maximum Profit: {profit_3}") # Expected output: 0
    print("-" * 20)

    # Example 4: Single price
    
    stock_prices_4 = [5]
    profit_4 = max_profit(stock_prices_4)
    print(f"Stock Prices: {stock_prices_4}")
    print(f"Maximum Profit: {profit_4}") # Expected output: 0
    print("-" * 20)

