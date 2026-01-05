# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(nlog(n))
# Space complexity: O(1)
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        result = 0
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                result += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1

        return result


if __name__ == '__main__':
    print(Solution().maxOperations([3,1,3,4,3], 6))