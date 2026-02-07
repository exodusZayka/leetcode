# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def dfs(node: TreeNode, left: int, right: int) -> None:
            self.max = max(self.max, left, right)
            if node.left:
                dfs(node.left, right + 1, 0)
            if node.right:
                dfs(node.right, 0, left + 1)

        dfs(root, 0, 0)
        return self.max
