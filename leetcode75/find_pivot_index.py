# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_sum = nums[:]
        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]
        for i in range(n):
            if prefix_sum[i] - nums[i] == prefix_sum[-1] - prefix_sum[i]:
                return i
        return -1


if __name__ == '__main__':
    print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
