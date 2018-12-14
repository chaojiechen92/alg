class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 需要优化下
        k = 0
        total = 0
        val = nums[0] if nums else 0
        for i, num in enumerate(nums):
            if num == val and total < 2:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
                total += 1
            elif num != val:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
                total = 1
                val = num
        return k

    def removeDuplicates2(self, nums, k):
        r = 0
        i = 0
        lens = len(nums)
        while i < lens:
            # r -k 精髓
            if r < 2 or nums[r - k] != nums[i]:
                nums[r] = nums[i]
                r += 1
            i += 1
        # print(r)
        return r


if __name__ == "__main__":
    l = [1, 1, 1, 2, 2, 3]
    Solution().removeDuplicates2(l, 2)
    print(l)
