# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        res = float('-inf')

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow
        while current:
            next_current = current.next
            current.next = prev
            prev = current
            current = next_current
        while prev:
            res = max(res, prev.val + head.val)
            head = head.next
            prev = prev.next
        return res


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(Solution().pairSum(head))
