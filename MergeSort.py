"""
归并排序

        8   4   5   7   1   3   6   2

分      8   4     5   7   |  1   3   6   2
        8   4  |  5   7
        8  | 4   5 | 7

治       4   8  |  5   7
         4   5    7   8

mySort:
    1.两个列表相互比较大小
    2.左边第0个和右边第0个比较大小,将小的数存入新列表L中,并将该值从原有列表弹出
    3.若某个列表为空，则直接将另一个列表其所有值直接添加到
"""

L = [2, 10, 9, 3, 4, 8, 7, 5, 1, 6]


def mySort(leftarray, rightarray):
    L = []
    if len(leftarray) == 0:
        L += rightarray
    if len(rightarray) == 0:
        L += leftarray
    if leftarray[0] <= rightarray[0]:
        L.append(leftarray.pop(0))
    else:
        L.append(rightarray.pop(0))
    return L


def merge(array):
    Length = len(array)
    if Length == 1:
        return array
    else:
        middle = Length // 2
        leftlist = merge(array[:middle])
        rightlist = merge(array[middle:])
        mySort(leftlist, rightlist)


print(merge(L))
