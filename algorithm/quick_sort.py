# __author: ioi
# date: 2021/8/26
# 快速排序
def quickSort(arr):
    # 基线条件
    if len(arr) < 2:
        return arr
    else:
        val = arr[0]
        less = [i for i in arr[1:] if i <= val]
        greater = [j for j in arr[1:] if j > val]
        return quickSort(less) + [val] + quickSort(greater)


if __name__ == '__main__':
    print(quickSort([5, 3, 6, 7, 9, 10, 1]))
