# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter

        counter_1 = Counter(word1)
        counter_2 = Counter(word2)
        if len(word1) != len(word2):
            return False
        if counter_1 == counter_2:
            return True
        return Counter(counter_1.values()) == Counter(counter_2.values()) and counter_1.keys() == counter_2.keys()


if __name__ == '__main__':
    print(Solution().closeStrings('aaabbbbccddeeeeefffff', 'aaaaabbcccdddeeeeffff'))
