class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i, v in enumerate(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums

if __name__ == "__main__":
    print(Solution().moveZeroes([0,1,0,3,13]))
