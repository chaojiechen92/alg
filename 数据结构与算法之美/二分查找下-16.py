# 查找第一个值等于给定值的元素
def bsearch_left(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] <= target:
            if mid - 1 < 0 or nums[mid - 1] < target: return mid
            high = mid - 1

        elif nums[mid] > target:
            low = mid + 1

    return -1


# 查找最后一个值等于给定值的元素
def bsearch_right(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] <= target:
            high = mid - 1

        elif nums[mid] > target:
            if mid + 1 > high or nums[mid + 1] < target: return mid
            low = mid + 1

    return -1


# 查找第一个大于等于给定值的元素
def bsearch_gt(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] >= target:
            if mid + 1 <= high and nums[mid] == target and nums[mid + 1] > target: return mid + 1
            low = mid + 1
        elif nums[mid] < target:
            high = mid - 1
    return -1


# 查找最后一个小于等于给定值的元素
def bsearch_lt(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > target:
            low = mid + 1
        elif nums[mid] <= target:
            if mid - 1 >= 0 and nums[mid] == target and nums[mid - 1] < target: return mid - 1
            high = mid - 1


# 思考题　leetcode 33 搜索旋转排序数组
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pass


if __name__ == "__main__":
    pass
