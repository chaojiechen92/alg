class Solution():
    def stackandstackSort(self, nums):
        '''

        :param list nums:
        :return:
        '''
        s = []

        while nums:
            val = nums.pop()
            while s and val > s[-1]:
                nums.append(s.pop())
            s.append(val)

        while s:
            nums.append(s.pop())
        return


if __name__ == "__main__":
    l  = [1,3,5,2]
    Solution().stackandstackSort(l)
    print(l)
