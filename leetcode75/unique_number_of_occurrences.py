# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

# For all solutions:
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d = {}
        for item in arr:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        return len(d.values()) == len(set(d.values()))


class DefaultDictSolution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        from collections import defaultdict

        d = defaultdict(int)
        for item in arr:
            d[item] += 1
        return len(d.values()) == len(set(d.values()))


class CounterSolution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        from collections import Counter

        d = Counter(arr)
        return len(d.values()) == len(set(d.values()))


if __name__ == '__main__':
    print(Solution().uniqueOccurrences([1,2]))
