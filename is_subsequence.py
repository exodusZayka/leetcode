# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n + m)
# Space complexity: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        first = second = 0
        while first < len(s) and second < len(t):
            if s[first] == t[second]:
                first += 1
            second += 1
        return first == len(s)


if __name__ == '__main__':
    s = "aaaaaa"
    t = "bbaaaa"

    print(Solution().isSubsequence(s, t))