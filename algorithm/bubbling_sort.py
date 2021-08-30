# __author: ioi
# date: 2021/8/21
# 冒泡排序
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == '__main__':
    print(bubble_sort([4, 1, 7, 3, 9, 0, 6]))
