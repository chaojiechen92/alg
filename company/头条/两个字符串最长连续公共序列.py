class Solution(object):
    # 错的

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        i = 1
        ret = []
        while i < lens - 1:
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                ret.append(i)
            i += 1

        return ret


if __name__ == "__main__":
    print(Solution().findPeakElement([1,2,1,3,5,6,4]))