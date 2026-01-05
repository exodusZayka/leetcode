# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        while left < right:
            result = max(result, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result


if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))