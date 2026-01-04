# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def compress(self, chars: list[str]) -> int:
        answer = 0
        i = 0
        while i < len(chars):
            letter = chars[i]
            group_len = 0
            while i < len(chars) and chars[i] == letter:
                group_len += 1
                i += 1

            chars[answer] = letter
            answer += 1
            if group_len > 1:
                for c in str(group_len):
                    chars[answer] = c
                    answer += 1

        return answer

chars = ["a","a","b","b","c","c","c"]
print(Solution().compress(chars))
print(chars)
