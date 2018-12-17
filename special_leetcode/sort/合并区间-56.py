# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # 基本算法
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        lens = len(intervals)
        intervals = sorted(intervals, key=lambda startone: startone.start)

        ret = []
        interval = intervals[0]
        i = 1
        while i < lens:
            if interval.end >= intervals[i].start:
                interval = Interval(interval.start, max(interval.end, intervals[i].end))
            else:
                ret.append(interval)
                interval = intervals[i]

            i += 1
        ret.append(interval)

        return ret

    # 解法2
    def merge2(self, intervals):
        pass


if __name__ == "__main__":
    pass
