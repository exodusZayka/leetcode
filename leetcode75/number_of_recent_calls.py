# https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75


class RecentCounter:
    def __init__(self):
        self._queue = []

    def ping(self, t: int) -> int:
        diff = 3000
        self._queue.append(t)
        i = 0
        for indx in range(-1, -len(self._queue) - 1, -1):
            if self._queue[indx] < t - diff:
                break
            i += 1
        return i


if __name__ == '__main__':
    obj = RecentCounter()
    param_1 = obj.ping(1)