# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Explanation: https://www.youtube.com/watch?v=bNvIQI2wAjk
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
    
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        
        return [prefix[i] * postfix[i] for i in range(n)]


print(Solution().productExceptSelf([-1,1,0,-3,3]))