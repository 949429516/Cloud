"""
二分查找
1.必须是排序后的列表
递归查找：
1.如果中间值>目标值说明目标值在中间值之前，则中间值为末尾
2.如果中间值<目标值说明目标值在中间值之后，则中间值为开头
"""
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def Search(array, startindex, endindex, num):
    """
    :param array: 需要查找的列表
    :param startindex: 列表开始的下标
    :param endindex: 列表结束的下标
    :param num: 需要查找的数字
    :return: 查找数字的下标
    """
    middle_index = (startindex + endindex) // 2
    # 判断查找的数字是否在列表内
    if startindex > endindex:
        return False
    middle_num = array[middle_index]
    if num == middle_num:
        return middle_index
    else:
        if num < middle_num:
            return Search(array, startindex, middle_index - 1, num)
        else:
            return Search(array, middle_index + 1, endindex, num)


print(Search(L, 0, len(L) - 1, 1))
