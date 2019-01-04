class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []

        def getsub(i):
            str = []
            s = 0
            while i > 0:
                if i & 0x1:
                    str.append(nums[s])
                i >>= 1
                s += 1
            return str

        for i in range(0, 2 ** len(nums)):
            ret.append(getsub(i))
        return ret


if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
