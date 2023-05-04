# QUESTION :
# You are given an array prices where prices[i] is the price of a given stock on the ith day.You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfitOfStock(prices):
    # Using the sliding window method(Two pointers)
    l = 0  # The first pointer will store the index of the lowest price
    r = 1  # The second pointer will store the index of the highest price
    maxProfit = 0  # The maxProfit will store the difference between highest price and lowest price

    # The loop continues until the last element of the prices array.
    while r < len(prices):
        if (prices[l] < prices[r]):  # If the index of the right pointer value in the prices array is less than the index of the left pointer value. Check if profit is higher than maxProfit
            profit = prices[r]-prices[l]
            # If profit is higher than maxProfit. Change profit to maxProfit
            maxProfit = max(profit, maxProfit)
        else:
            # If the index of the right pointer value in the prices array is less than the index of the left pointer value. Replace the index of the left pointer with the index of the right pointer.
            l = r
        # Increase r to 1 for each cycle
        r += 1
    return maxProfit


print('Output:', maxProfitOfStock([7, 1, 5, 3, 6, 4]))
# Output: 5
print('Output:', maxProfitOfStock([7, 6, 4, 3, 1]))
# Output: 0
