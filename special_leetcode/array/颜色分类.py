class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # max_arr = []
        # maxs = max(nums)
        # for n in range(0, maxs + 1):
        #     max_arr.append(0)
        #
        # for n in nums:
        #     max_arr[n] += 1
        #
        # i = 1
        # while i < len(max_arr):
        #     max_arr[i] = max_arr[i] + max_arr[i - 1]
        #     i += 1

        ret = []
        # for n in nums:
        low, high = 0, len(nums) - 1
        i = 0
        while i <= high:
            if nums[i] < 1:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1
                i += 1
            elif nums[i] > 1:
                nums[high], nums[i] = nums[i], nums[high]
                high -= 1
            else:
                i += 1
        return nums
        # for i, v in enumerate(nums):
        #     if v == 0:
        #         nums[low], nums[i] = nums[i], nums[low]
        #         low += 1
        #     elif v == 2:
        #         nums[high], nums[i] = nums[i], nums[high]
        #         high -= 1


if __name__ == "__main__":
    print(Solution().sortColors([2, 0, 2, 1, 1, 0]))
