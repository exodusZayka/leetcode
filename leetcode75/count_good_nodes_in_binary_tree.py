# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, float('-inf'))]

        while stack:
            node, maxval = stack.pop()
            if node.val >= maxval:
                res += 1
            if node.left:
                stack.append((node.left, max(maxval, node.val)))
            if node.right:
                stack.append((node.right, max(maxval, node.val)))
        return res


if __name__ == '__main__':
    root = TreeNode(
        3,
        TreeNode(
            1,
            TreeNode(3),
        ),
        TreeNode(
            4,
            TreeNode(1),
            TreeNode(5)
        ),
    )
    print(Solution().goodNodes(root))
