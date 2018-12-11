class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        ret = 0
        while i < 64:
            k = 0
            mask = (1 << i)
            for n in nums:
                if n & mask:
                    k += 1
            if k % 3:
                ret |= mask
            i += 1

        return ret


if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 3, 2]))
