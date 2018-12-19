def bsearch(nums, target):
    '''

    :param list[int] nums:
    :return:
    '''
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    print(bsearch([1, 2, 3, 4, 5], 4))
