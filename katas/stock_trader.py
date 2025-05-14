def max_profit(prices):
    """
    Finds the maximum profit that can be achieved by buying and selling the stock ONCE.

    Aim for O(n)

    Args:
        prices: a list of prices on each day

    Returns:
        the maximum profit, or 0 if no profit can be achieved
    """
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    # Loop through prices once - O(n) time complexity
    for price in prices:
        # Update minimum price seen so far
        if price < min_price:
            min_price = price
        # Calculate potential profit if we sell at current price
        current_profit = price - min_price
        # Update maximum profit if current profit is greater
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit


if __name__ == '__main__':
    stock_prices = [7, 1, 5, 3, 6, 4]
    profit = max_profit(stock_prices)
    print(f"Maximum Profit: {profit}")  # should be 5

    # Additional test cases
    prices1 = [7, 6, 4, 3, 1]
    print(f"Maximum Profit: {max_profit(prices1)}")  # should be 0 (no profit possible)

    prices2 = [1, 2, 3, 4, 5]
    print(f"Maximum Profit: {max_profit(prices2)}")  # should be 4 (buy at 1, sell at 5)