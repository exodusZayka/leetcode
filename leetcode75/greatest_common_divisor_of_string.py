# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75


# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         # My own solution
#         pattern = str2
#         while pattern:
#             if len(str1) % len(pattern) == 0 and len(str2) % len(pattern) == 0:
#                 if (
#                     pattern * (len(str1) // len(pattern)) == str1
#                     and pattern * (len(str2) // len(pattern)) == str2
#                 ):
#                     return pattern
#             pattern = pattern[:-1]

#         return ''


# Time complexity: O(len(str1) + len(str2)), because on the line 27 we create 2 objects
# and compare them letter by letter
# Space complexity: O(len(str1) + len(str2)), because on the line 26 we create 2 objects
# to compare str1 + str2 and str2 + str1
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # The Euclid's algorithm
        if str1 + str2 != str2 + str1:
            return ''
        
        def euclid_gcd(a: int, b: int):
            # Time complexity of this algo: O(log(min(len(str1), len(str2))))
            while b:
                a, b = b, b % a
            return a

        return str1[:euclid_gcd(len(str1), len(str2))]


print(Solution().gcdOfStrings('ababab', 'ab'))