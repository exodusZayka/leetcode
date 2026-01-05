# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = ('a', 'e', 'i', 'o', 'u')
        left, right = 0, len(s_list) - 1
        while left <= right:
            if s_list[left].lower() not in vowels:
                left += 1
                continue
            if s_list[right].lower() not in vowels:
                right -= 1
                continue
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return ''.join(s_list)


print(Solution().reverseVowels('leetcode'))