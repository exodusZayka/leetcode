# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if len(nums) == 1:
            return
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1

            fast += 1



if __name__ == '__main__':
    nums = [4,2,4,0,0,3,0,5,1,0]

    Solution().moveZeroes(nums)
    print(nums)
