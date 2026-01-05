# https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(n)
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         non_empty_plots = {i for i in range(len(flowerbed)) if flowerbed[i] == 1}
#         for i in range(len(flowerbed)):
#             if i == 0 and len(flowerbed) > 1:
#                 if not non_empty_plots.intersection({i, i + 1}):
#                     non_empty_plots.add(0)
#                     n -= 1
#             if i == len(flowerbed) - 1:
#                 if not non_empty_plots.intersection({i - 1, i}):
#                     non_empty_plots.add(i)
#                     n -= 1
#             if not non_empty_plots.intersection({i - 1, i, i + 1}):
#                 non_empty_plots.add(i)
#                 n -= 1
#         return n <= 0


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i - 1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            if left and flowerbed[i] == 0 and right:
                n -= 1
                flowerbed[i] = 1
        return n <= 0


print(Solution().canPlaceFlowers([0,0,1,0,0], 1))