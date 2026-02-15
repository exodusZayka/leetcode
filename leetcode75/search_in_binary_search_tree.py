# https://leetcode.com/problems/search-in-a-binary-search-tree/description/?envType=study-plan-v2&envId=leetcode-75


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(log(n))
# Space complexity: O(1)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if node.val == val:
                return node
            elif val < node.val:
                node = node.left
            else:
                node = node.right
        return None


if __name__ == '__main__':
    target_node =  TreeNode(4)
    tree = TreeNode(
        5,
        TreeNode(
            2,
            TreeNode(1, TreeNode(0)),
            TreeNode(3, None, target_node)
        ),
        TreeNode(
            8,
            TreeNode(7),
            TreeNode(10, TreeNode(9))
        )
    )
    print(Solution().searchBST(tree, target_node.val) == target_node)
