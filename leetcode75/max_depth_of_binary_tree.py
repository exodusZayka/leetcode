# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
# Space complexity: O(n) for the worst case (because of function call stack)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    print(Solution().maxDepth(root=root))
