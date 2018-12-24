import heapq


class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        i = 0
        self.k = k
        self.vector = []
        while i < k:
            self.vector.append(nums.pop(0))
            i += 1

        self.vector = sorted(self.vector)
        while nums:
            val = nums.pop(0)
            if val > self.vector[0]:
                self.vector[0] = val
                i = 0
                while i + 1 < k and self.vector[i] > self.vector[i + 1]:
                    self.vector[i], self.vector[i + 1] = self.vector[i + 1], self.vector[i]
                    i += 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if val > self.vector[0]:
            self.vector[0] = val
            i = 0
            while i + 1 < self.k and self.vector[i] > self.vector[i + 1]:
                self.vector[i], self.vector[i + 1] = self.vector[i + 1], self.vector[i]
                i += 1
        return self.vector[0]


# 使用优先队列
class KthLargest2:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.h = []
        i = 0
        while i < k:
            heapq.heappush(self.h, nums.pop(0))
            i += 1

        while nums:
            val = nums.pop(0)
            if val > self.h[0]:
                heapq.heappushpop(self.h, val)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if val > self.h[0]:
            heapq.heappushpop(self.h, val)

        return self.h[0]


if __name__ == "__main__":
    k = 3
    arr = [4, 5, 8, 2]
    kq = KthLargest(k, arr)
    print(kq.add(3))
    print(kq.add(5))
    print(kq.add(10))
    print(kq.add(9))
    print(kq.add(4))
