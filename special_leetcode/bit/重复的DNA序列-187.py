class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {
            "A": 0,
            "C": 1,
            "G": 2,
            "T": 3
        }
        d2 = set()
        i = 0
        src = 0
        while i < 9:
            src |= d[s[i]]
            src <<= 2
            i += 1
        ret = []
        while i < len(s):
            src <<= 2
            src |= d[s[i]]
            src &= 0xFFFFF
            if src in d2:
                ret.append(src)
            else:
                d2.add(src)
            i += 1
        return ret


if __name__ == "__main__":
    print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
