class Solution:
    # O(n^2) 最孬的算法
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lens = len(nums)
        i = 1
        while i < lens:
            j = i - 1
            val = nums[i]
            while j >= 0 and nums[j] < val:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = val
            i += 1
        return nums[k - 1]

    # 选择排序
    def findKthLargest2(self, nums, k):
        i = 0
        lens = len(nums)
        res = 0
        while i < k:
            j = 0
            while j < lens - i - 1:
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j += 1
            res = nums[j]

            i += 1
        return res

    # 快排思想
    def findKthLargest3(self, nums, k):
        def partion(nums, s, e):
            j = s
            val = nums[e]
            while s <= e - 1:
                if nums[s] > val:
                    nums[j], nums[s] = nums[s], nums[j]
                    j += 1
                s += 1
            nums[e], nums[j] = nums[j], nums[e]
            return j

        mid = partion(nums, 0, len(nums) - 1)
        while mid != k - 1:
            if mid > k - 1:
                mid = partion(nums, 0, mid - 1)
            elif mid < k - 1:
                mid = partion(nums, mid + 1, len(nums)-1)

        return nums[mid]
    # 　优先队列的思   路解决大输入情况


if __name__ == "__main__":
    print(Solution().findKthLargest3([3, 2, 1, 5, 6, 4], 2))
