class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n ==0 or n & n - 1 else True


if __name__ == "__main__":
    pass
