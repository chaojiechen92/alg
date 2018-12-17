class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if not s or not t: return False
        if len(s) != len(t): return False
        d1, d2 = {}, {}
        for c in s:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1

        for c in t:
            if c in d2:
                d2[c] += 1
            else:
                d2[c] = 1

        for c, v in d1.items():
            if c not in d2 or d2[c] != v:
                return False
        return True


if __name__ == "__main__":
    pass
