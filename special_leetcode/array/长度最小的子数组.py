class Solution:
    # 暴力法　O(n^2)
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
       """
        # if not nums:
        #     return 0
        lens = len(nums)
        ret = lens + 1
        i = 0
        while i < lens:
            j = i + 1
            sum = nums[i]
            while j < lens and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s and ret > j - i:
                ret = j - i
            i += 1
        return ret if ret <= lens else 0

    def minSubArrayLen2(self, s, nums):
        lens = len(nums)
        r, l = 0, 0
        sum_all = 0
        min_len = lens + 1
        while l < lens:
            if r < lens and sum_all < s:
                sum_all += nums[r]
                r += 1
            else:
                sum_all -= nums[l]
                l += 1
            if sum_all >= s and r - l < min_len:
                min_len = r - l

        return min_len if min_len <= lens else 0


if __name__ == "__main__":
    print(Solution().minSubArrayLen2(7, [2, 3, 1, 2, 4, 3]))
