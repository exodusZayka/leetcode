# https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n ^ 2)
# Space complexity: O(n)
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        from collections import Counter

        n = len(grid)
        row_counter = Counter(map(tuple, grid))
        result = 0
        for i in range(n):
            column = []
            for row in grid:
                column.append(row[i])
            result += row_counter.get(tuple(column), 0)
        return result

if __name__ == '__main__':
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(Solution().equalPairs(grid))
