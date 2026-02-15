from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.val


# Time complexity: O(n)
# Space complexity: O(n). For description see max_level_sum_in_binary_tree.py file
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            right_side = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    right_side = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right_side:
                result.append(right_side.val)

        return result


if __name__ == '__main__':
    root = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4, TreeNode(5)),
            None,
        ),
        TreeNode(
            3,
            TreeNode(4),
        )
    )
    print(Solution().rightSideView(root))
