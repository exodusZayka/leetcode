# https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # Explanation: https://www.youtube.com/watch?v=i340M1N4i8Y
        min = max = float('inf') 
        for n in nums:
            if n <= min:
                min = n
            elif n <= max:
                max = n
            else:
                return True
        return False

print(Solution().increasingTriplet([2,1,5,0,4,6]))
