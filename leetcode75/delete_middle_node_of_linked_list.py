# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not (head and head.next):
            head = None
            return head
        prev = ListNode(0, head)
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head

if __name__ == '__main__':
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
    head = ListNode(1)
    Solution().deleteMiddle(head)
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next
