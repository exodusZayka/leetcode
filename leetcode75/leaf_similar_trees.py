# https://leetcode.com/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
# Space complexity: O(n) for the worst case
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collect_leaf_values(root: TreeNode) -> list:
            stack = [root]
            leaves = []
            while stack:
                node = stack.pop()
                if not (node.left or node.right):
                    leaves.append(node.val)
                    continue
                for child in [node.left, node.right]:
                    if child:
                        stack.append(child)
            return leaves

        return collect_leaf_values(root1) == collect_leaf_values(root2)


if __name__ == '__main__':
    root1 = TreeNode(
        1,
        TreeNode(2)
    )

    root2 = TreeNode(
        2,
        TreeNode(2)
    )
    print(Solution().leafSimilar(root1, root2))

















