# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer_1 = pointer_2 = 0
        res = []
        while pointer_1 < len(word1) or pointer_2 < len(word2):
            if pointer_1 < len(word1):
                res.append(word1[pointer_1])
                pointer_1 += 1
            if pointer_2 < len(word2):
                res.append(word2[pointer_2])
                pointer_2 += 1
        return ''.join(res)
