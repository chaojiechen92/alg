class Solution:
    # 暴力法　O(n^2)
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
       """
        lens = len(nums)
        i = 0
        ret = lens + 1
        while i < lens:
            j = i + 1
            sums = nums[i]
            while j < lens and sums < s:
                sums += nums[j]
                j += 1

            if sums >= s and ret > j - i:
                ret = j - i
            i += 1
        return ret if ret < lens else 0

    def minSubArrayLen2(self, s, nums):
        lens = len(nums)
        l1, l2 = 0, 0
        ret = lens + 1
        sums = 0
        # 多画图
        while l1 < lens or l2 < lens:
            if l1 < lens and sums < s:
                sums += nums[l1]
                l1 += 1
            else:
                if sums >= s and ret > l1 - l2:
                    ret = l1 - l2
                sums -= nums[l2]
                l2 += 1
        return ret if ret < lens else 0


if __name__ == "__main__":
    print(Solution().minSubArrayLen2(7, [2, 3, 1, 2, 4, 3]))
