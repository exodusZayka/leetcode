# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75


from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
# Space complexity: O(n)
# In fact, it is O(2 ** h), where h - the depth of the tree.
# If we consider the tree is completed (worst case), the number of leaves will be equal to 2 ** h.
# We also have the mathematical formula of total number of nodes: n = 2 ** (h + 1) - 1,
# Simplifying the formula, we'll get: n = 2 ** h.
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        level_number = 0
        max_tuple: tuple = (level_number, float('-inf'))

        while queue:
            current_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_number += 1

            current_sum = sum(current_level)
            max_tuple = max_tuple if max_tuple[1] > current_sum else (level_number, current_sum)
        return max_tuple[0]


if __name__ == '__main__':
    tree = TreeNode(
        10,
        TreeNode(
            -2,
            TreeNode(4),
            TreeNode(6, TreeNode(-7))
        ),
        TreeNode(
            8,
            TreeNode(13, None, TreeNode(15))
        )
    )
    print(Solution().maxLevelSum(tree))
