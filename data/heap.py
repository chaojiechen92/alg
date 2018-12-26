'''
    堆的性质
    1. 堆中的任意节点的值总是不大于（不小于）其子节点的值
    2. 堆是完全树结构
'''


class MinHeap():
    def __init__(self):
        self.heap = []

    def push(self, data):
        self.heap.append(data)
        lens = len(self.heap)
        end = lens - 1

        # 由下向上调整
        while end > 0:
            parent = (end - 1) >> 1
            if self.heap[parent] <= data:
                break

            self.heap[end] = self.heap[parent]
            end = parent

        self.heap[end] = data

        return

    def popmin(self):
        if not self.heap:
            return None
        ret = self.heap[0]
        val = self.heap.pop()
        # 第一版
        # while i < len(self.heap):
        #     left = 2 * i + 1
        #     if left < len(self.heap):
        #         if left < len(self.heap) - 1 and self.heap[left] > self.heap[left + 1]:
        #             left += 1
        #         if self.heap[i] <= self.heap[left]:
        #             break
        #         self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
        #     i = left

        # 优化版
        i = 0
        left = 1
        while left < len(self.heap):
            if left + 1 < len(self.heap) and self.heap[left] > self.heap[left + 1]:
                left += 1
            if val <= self.heap[left]:
                break
            self.heap[i] = self.heap[left]
            i = left
            left = left * 2 + 1

        self.heap[i] = val

        return ret

    def remove(self, data):
        i = self.index(data)
        if i == -1:
            return

        val = self.heap.pop()
        while i > 0:
            parent = (i - 1) >> 1
            if self.heap[parent] <= self.heap[i]:
                break
            self.heap[i] = self.heap[parent]
            i = parent

        self.heap[i] = val
        return

    def index(self, data):
        for i, v in enumerate(data):
            if v == data:
                return i
        return -1

    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    pass
