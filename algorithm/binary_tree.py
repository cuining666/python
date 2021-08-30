# __author: ioi
# date: 2021/8/29
# 二叉树查询
def binarySearch(arr, key):
    lowIndex = 0
    upperIndex = len(arr) - 1
    while True:
        curr = (lowIndex + upperIndex) // 2
        if arr[curr] == key:
            return curr
        elif arr[curr] < key:
            lowIndex = curr + 1
        elif arr[curr] > key:
            upperIndex = curr - 1


if __name__ == '__main__':
    print(binarySearch([1, 2, 3, 4, 5, 6], 4))
