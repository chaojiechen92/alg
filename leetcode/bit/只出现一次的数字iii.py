class Solution:
    # 解法１　时间复杂度 n 空间复杂度 n
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        ret = []

        for v, n in d.items():
            if n == 1:
                ret.append(v)
        return ret

    def singleNumber2(self, nums):
        '''

        :param nums:
        :return:
        '''
        v = 0
        for n in nums:
            v ^= n

        mask = 0x1
        while not v & mask:
            mask <<= 1

        one, two = 0, 0
        for n in nums:
            if n & mask:
                one ^= n
            else:
                two ^= n

        return [one, two]


if __name__ == "__main__":
    print(Solution().singleNumber2([1, 2, 1, 3, 2, 5]))
