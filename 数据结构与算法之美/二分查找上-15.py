'''

    二分查找
    局限性
    1. 依赖有序的数组
    2. 数据量太小不适合二分查找　顺序遍历够了
    3. 数据量太大也不适合，数组是连续的内存空间，对内存的要求比较苛刻


'''

def bsearch(nums,target):
    '''

    :param list nums:
    :return:
    '''
    low,high = 0, len(nums)-1
    while low <= high:
        mid = low+ ((high-low)>>1)
        if nums[mid]< target:
            low = mid+1
        elif nums[mid]>target:
            high = mid-1
        else:
            return mid

    return -1


#课后习题　求一个数的平方根,要求精确到小数点的后６位
def mysqrt(x,stopvalue=0.000001):

    low, high = 0,x
    mid = x/2
    while abs(mid**2 - x) > stopvalue:

        if mid**2 > x:
            high =mid
        elif mid**2 < x:
            low = mid

        mid = (high+low)/2
    return mid

# 如果数据使用链表存储，二分查找的时间复杂度是多少
# O(n) n/2 +n/4+....+1 O(2n-1)

if __name__ == "__main__":
    print(mysqrt(9))