# https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        res = max(0, gain[0])
        for i in range(1, len(gain)):
            gain[i] += gain[i - 1]
            res = max(res, gain[i])
        return res


if __name__ == '__main__':
    print(Solution().largestAltitude([-4,-3,-2,-1,4,3,2]))
