# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


# My custom solution based on 2 pointers and comparison them to infinity.
# Explanation: https://www.youtube.com/watch?v=i340M1N4i8Y
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_value = max_value = float('inf')
        result = 0
        for current in prices:
            if current < min_value:
                min_value = current
                max_value = current
            elif current > max_value:
                max_value = current
            result = max(result, max_value - min_value)
        return result


# A little bit of different solution using sliding window.
# Explanation: https://www.youtube.com/watch?v=1pkOgXD63yU&list=PLot-Xpze53leOBgcVsJBEGrHPd_7x_koV
# Time complexity: O(n)
# Space complexity: O(1)
class SlidingWindowSolution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        result = 0
        left, right = 0, 1
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
            elif profit > result:
                result = profit
            right += 1

        return result


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    custom_max_profit = Solution().maxProfit(prices)
    sliding_window_max_profit = SlidingWindowSolution().maxProfit(prices)
    print(custom_max_profit == sliding_window_max_profit)
