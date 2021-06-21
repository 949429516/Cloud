"""
冒泡排序

第一个数字和第二个数字比较：
   index0 > index1交换位置否则不变
第二个和第三个比较,以此类推
每一轮结束,列表最后的数字就是当前最大的,下次不再参与比较
"""

L = [2, 10, 9, 3, 4, 8, 7, 5, 1, 6]


def bubble(array):
    Length = len(array)
    originIndex = Length - 1
    n = 1
    while n < Length:
        for index in range(originIndex):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
        n += 1
        originIndex -= 1
    return array


print(bubble(L))
