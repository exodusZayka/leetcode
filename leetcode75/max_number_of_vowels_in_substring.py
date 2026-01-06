# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        result = 0
        current_result = 0
        for i in range(len(s)):
            if i >= k:
                if s[i - k] in vowels:
                    current_result -= 1
            if s[i] in vowels:
                current_result += 1
            result = max(result, current_result)
        return result


if __name__ == '__main__':
    print(Solution().maxVowels('leetcode', 3))