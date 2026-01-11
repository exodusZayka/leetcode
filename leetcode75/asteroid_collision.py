# https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack


if __name__ == '__main__':
    print(Solution().asteroidCollision([8, -8]))
