# https://leetcode.com/problems/dota2-senate/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque

        n = len(senate)
        R = deque()
        D = deque()
        for indx, value  in enumerate(senate):
            if value == 'R':
                R.append(indx)
            else:
                D.append(indx)
        while R and D:
            r = R.popleft()
            d = D.popleft()
            if r < d:
                R.append(r + n)
            else:
                D.append(d + n)

        return 'Radiant' if R else 'Dire'


if __name__ == '__main__':
    print(Solution().predictPartyVictory('RDD'))