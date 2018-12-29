import heapq


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h = []
        i = 0
        # while i < k:
        #     heapq.heappush(h, (-nums[i], i))
        #     i += 1

        ret = []
        while i < len(nums):

            heapq.heappush(h, (-nums[i], i))
            val = h[0]
            while val[1] <= i - k:
                heapq.heappop(h)
                val = h[0]
            if i >= k - 1:
                ret.append(-h[0][0])

            i += 1

        return ret


if __name__ == "__main__":
    print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
