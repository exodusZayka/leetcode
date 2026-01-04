# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75


# Custom solution without .split()
# Time complexity: O(n ^ 2)
# Space complexity: O(n)
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         i = 0
#         result = []
#         while i < len(s):
#             if s[i] != ' ':
#                 if i == 0 or s[i - 1] == ' ':
#                     result.append(s[i])
#                 else:
#                     result[-1] += s[i]
#             i += 1
#         return ' '.join(result[::-1])


# Builtin solution
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        splitted_s = s.split()
        return ' '.join(splitted_s[::-1])

print(Solution().reverseWords("a good   example") == 'example good a')