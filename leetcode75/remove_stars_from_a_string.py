# https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        return ''.join(stack)


if __name__ == '__main__':
    print(Solution().removeStars('erase*****'))
