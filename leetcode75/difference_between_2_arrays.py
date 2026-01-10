# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n + m)
# Space complexity: O(n + m)
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        # Or we can also use set_1 - set_2, set_2 - set_1 - it doesn't matter
        difference_1 = set(nums1).difference(nums2)
        difference_2 = set(nums2).difference(nums1)
        return [list(difference_1), list(difference_2)]


if __name__ == '__main__':
    print(Solution().findDifference([1,2,3,3], [1,1,2,2]))
