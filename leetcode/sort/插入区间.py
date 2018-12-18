# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return str(self.start) + '|' + str(self.end)


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ret = []
        lens = len(intervals)
        i = 0
        while i < lens:
            if newInterval.end >= intervals[i].start and intervals[i].end >= newInterval.start:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
            elif newInterval.end < intervals[i].start:
                ret.append(newInterval)
                newInterval = intervals[i]
            else:
                ret.append(intervals[i])
            i += 1
        ret.append(newInterval)
        return ret


if __name__ == "__main__":
    print(Solution().insert([Interval(1, 3), Interval(6, 9), Interval(10, 12)], Interval(13, 15)))
