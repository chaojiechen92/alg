class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = sorted(nums)
        low, high = 0, len(nums) - 1

        while low < high:
            if nums[low] + nums[high] < target:
                low += 1
            elif nums[low] + nums[high] > target:
                high -= 1
            else:
                return [low, high]
        return []

    def twoSum2(self, nums, target):
        d = {}
        for i, v in enumerate(nums):
            if v in d:
                return [d[v], i]
            d[target - v] = i
        return []


if __name__ == "__main__":
    print(Solution().twoSum2([2, 7, 11, 15], 9))
