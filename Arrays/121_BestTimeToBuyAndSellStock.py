'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

'''
Brief Approach:

- Initialize variables min and max to represent the minimum and maximum prices encountered during the iteration.
- Initialize a variable maxprofit to 0, representing the maximum profit.
- Iterate through each price in the prices list.
- If the current price is less than the current minimum (price < min), update the minimum (min = price) and reset the maximum (max = 0).
- If the current price is greater than the current maximum (price > max), update the maximum (max = price) and calculate the profit (max - min).
- If the calculated profit is greater than the current maxprofit, update maxprofit with the new value.
- After the loop, return the calculated maxprofit as the result.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min=99999
        max=0
        maxprofit=0
        for price in prices:
            if price<min:
                min=price
                max=0
            if price>max:
                max=price
                if max-min>maxprofit:
                    maxprofit=max-min
        return maxprofit
