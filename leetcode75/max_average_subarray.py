# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        result = current_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            result = max(result, current_sum)

        return result / k


if __name__ == '__main__':
    print(Solution().findMaxAverage([5], 1))