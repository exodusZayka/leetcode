# https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []

        for indx, char in enumerate(s):
            if char != ']':
                string_stack.append(char)
            else:
                curr_string = ''
                while string_stack[-1] != '[':
                    curr_string = string_stack.pop() + curr_string

                string_stack.pop()
                current_number = ''
                while string_stack and string_stack[-1].isdigit():
                    current_number = string_stack.pop() + current_number
                string_stack.append(curr_string * int(current_number))
        return ''.join(string_stack)


if __name__ == '__main__':
    print(Solution().decodeString('3[a2[c]]'))
