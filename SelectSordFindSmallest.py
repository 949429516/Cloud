"""
选择排序：
    将列表按照从小到大的顺序排序
分为两个函数:
    def findsmallest 寻找当前列表中最小的值
    def selection 将findsmallest中返回的值添加到新列表中，再从原始列表中删除
"""

def findsmallest(arr):
    """
    找到当前列表中最小值
    :param arr: 目标列表
    :return: 当前列表中最小值的下标
    """
    smallest = arr[0]    # 存储最小值
    smallest_index = 0   # 存储最小值的索引
    for index in range(1, len(arr)):
        if arr[index] < smallest:
            smallest = arr[index]
            smallest_index = index
    return smallest_index


def selectionSort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr


print(selectionSort([3, 8, 6, 2, 1, 3, 9, 10]))