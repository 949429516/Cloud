"""
插入排序

1.从数组的第二个数据开始往前比较，即一开始用第二个数和他前面的一个比较，如果符合条件（比前面的大或者小，自定义），则让他们交换位置。

2.然后再用第三个数和第二个比较，符合则交换，但是此处还得继续往前比较直到比较到第一个数

3.重复1和2直到最后一个数字开始
"""

L = [2, 10, 9, 3, 4, 8, 7, 5, 1, 6]


def Insert(array, index):

    while index > 0:
        if array[index] < array[index - 1]:
            array[index], array[index - 1] = array[index - 1], array[index]
        else:
            break
        index -= 1
    return array


def Sort(array):
    Length = len(array)
    L = array
    for index in range(1, Length):
        L = Insert(L, index)
    return L


print(Sort(L))
