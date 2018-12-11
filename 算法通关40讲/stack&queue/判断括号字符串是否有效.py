class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        op_set = set(["(", ")", "{", "}", "[", "]"])

        stack = []
        for c in s:
            if c in op_set:
                if c not in d:
                    stack.append(c)
                elif not stack or d[c] != stack.pop():
                    return False
        return not stack


if __name__ == "__main__":
    print(Solution().isValid("222(ss*ds("))
