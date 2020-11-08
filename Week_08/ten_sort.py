"""
    经典排序算法
"""


# 冒泡排序
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 选择排序
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# 插入排序
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# 希尔排序
def shellSort(arr):
    n = len(arr)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            tmp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > tmp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = tmp
        gap = int(gap / 2)


# 归并排序
def merge(left, right):
    ret = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ret.append(left[i])
            i += 1
        else:
            ret.append(right[j])
            j += 1
    ret += left[i:]
    ret += right[j:]
    return ret


def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = int(n / 2)
    left = mergeSort(arr[: mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)


# 快速排序
def quickSort(arr, i, j):
    if i >= j:
        return []
    pivot = arr[i]
    low = i
    high = j
    while i < j:
        if arr[j] >= pivot:
            j -= 1
        arr[i] = arr[j]
        if arr[i] <= pivot:
            i += 1
        arr[j] = arr[i]
    arr[j] = pivot
    quickSort(arr, low, i - 1)
    quickSort(arr, i + 1, high)
    return arr


# 堆排序
def heapSort(arr: list, num: int):
    import heapq
    heapq.heapify(arr)
    heapq.heappush(arr, num)  # 添加元素
    return [heapq.heappop(arr) for _ in range(len(arr))]


# 计数排序
def countSort(arr):
    output = [0 for _ in range(256)]
    count = [0 for _ in range(256)]
    ans = ["" for _ in arr]

    for i in arr:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


# 桶排序

class bucketSort(object):
    def _max(self, oldlist):
        _max = oldlist[0]
        for i in oldlist:
            if i > _max:
                _max = i
        return _max

    def _min(self, oldlist):
        _min = oldlist[0]
        for i in oldlist:
            if i < _min:
                _min = i
        return _min

    def sort(self, oldlist):
        _max = self._max(oldlist)
        _min = self._min(oldlist)
        s = [0 for i in range(_min, _max + 1)]
        for i in oldlist:
            s[i - _min] += 1
        current = _min
        n = 0
        for i in s:
            while i > 0:
                oldlist[n] = current
                i -= 1
                n += 1
            current += 1

    def __call__(self, oldlist):
        self.sort(oldlist)
        return oldlist


# 基数排序
def radixSort(arr, num):
    for k in range(num):  # 几位数决定有几轮排序
        s = [[] for _ in range(10)]
        for i in arr:
            s[i / (10 ** k) % 10].append(i)
        arr = [a for b in s for a in b]
    return arr


if __name__ == '__main__':
    # array = [64, 25, 12, 22, 11]
    array = [12, 34, 54, 2, 3]
    # selectionSort(array)
    # insertionSort(array)
    # shellSort(array)
    # ret = mergeSort(array)
    # print(array)
    # print(ret)

    # lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    # print("排序前的序列为：")
    # for i in lists:
    #     print(i, end=" ")
    # print("\n排序后的序列为：")
    # for i in quickSort(lists, 0, len(lists) - 1):
    #     print(i, end=" ")

    hs = heapSort(array, 10)
    print(hs)
