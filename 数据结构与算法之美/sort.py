class Solution():
    # 稳定的排序
    def bucket_sort(self, nums):
        '''

        :param list nums:
        :return:
        '''
        maxs = max(nums)
        maxs_bucket = []
        for i in range(0, maxs + 1):
            maxs_bucket.append(0)

        for n in nums:
            maxs_bucket[n] += 1

        i = 0
        for v, counter in enumerate(maxs_bucket):
            while counter > 0:
                nums[i] = v
                counter -= 1
                i += 1

        return

    # 稳定的排序
    def countiong_sort(self, nums):
        '''

        :param list nums:
        :return:
        '''
        maxs = max(nums)
        maxs_bucket = []
        for i in range(0, maxs + 1):
            maxs_bucket.append(0)

        for n in nums:
            maxs_bucket[n] += 1
        sum = 0
        for i, n in enumerate(maxs_bucket):
            maxs_bucket[i] = sum + n
            sum = maxs_bucket[i]

        c = [0 for n in range(0, len(nums))]
        for n in nums:
            c[maxs_bucket[n] - 1] = n
            maxs_bucket[n] -= 1
        return c

    def radix_sort(self):
        '''
        基数排序对要排序的数据是有要求的，需要分割出独立的位，位之间有递进关系,位数基本相同
        :return:
        '''
        pass

    def task(self, string: str):
        '''
        假设我们现在需要对 D，a，F，B，c，A，z 这个字符串进...
        '''
        nums = range(48, 58)
        lower_l = range(97, 123)
        upper_l = range(65, 91)

        arr = [[], [], []]
        for c in string:
            if ord(c) in nums:
                arr[0].append(c)
            elif ord(c) in lower_l:
                arr[1].append(c)
            elif ord(c) in upper_l:
                arr[2].append(c)

        ret = ''
        for a in arr:
            for c in a:
                ret += c

        return ret


if __name__ == "__main__":
    l = [2, 1, 4, 3, 3]
    # Solution().bucket_sort(l)
    # print(Solution().countiong_sort(l))
    print(Solution().task("a12dF3d"))
