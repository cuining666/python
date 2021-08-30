# __author: ioi
# date: 2021/8/21
# 选择排序
def findSmallest(nums):
    smallest = nums[0]
    smallest_index = 0
    for i in range(1, len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
            smallest_index = i
    return smallest_index


def selectSort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr


def sumArr(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        val = arr.pop(0)
        return val + test(arr)


if __name__ == '__main__':
    print(selectSort([4, 1, 7, 3, 9, 0, 6]))
    print(sumArr([4, 4, 5, 6, 6]))
