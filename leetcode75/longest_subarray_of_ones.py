# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        allow_to_delete = 1
        left = result = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                allow_to_delete -= 1
            while allow_to_delete < 0:
                if nums[left] == 0:
                    allow_to_delete += 1
                left += 1
            result = max(result, right - left)

        return result


if __name__ == '__main__':
    print(Solution().longestSubarray([1, 1, 1]))