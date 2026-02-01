# https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n ^ 2)
# Space complexity: O(n ^ 2)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        res = 0
        stack = [(root, root.val)]
        while stack:
            node, current_sum = stack.pop()
            if current_sum == targetSum:
                res += 1
            if node.left:
                stack.append((node.left, node.left.val + current_sum))
            if node.right:
                stack.append((node.right, node.right.val + current_sum))
        return res + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)


if __name__ == '__main__':
    root = TreeNode(
        10,
        TreeNode(
            5,
            TreeNode(
                3,
                TreeNode(3),
                TreeNode(-2)
            ),
            TreeNode(
                2,
                None,
                TreeNode(1)
            )
        ),
        TreeNode(
            -3,
            None,
            TreeNode(11)
        )
    )
    print(Solution().pathSum(root, 1))
