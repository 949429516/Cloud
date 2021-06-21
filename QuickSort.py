"""
快速排序

找到一个基准值piovt

小于基准值less

大于基准值greater

排序后的列表= less + piovt + greater
"""
L = [2, 10, 9, 3, 4, 8, 7, 5, 1, 6]

def quicksort(array):
    if len(array) < 2:
        return array # 基线条件:为空或者只有一个值的时候
    else:
        piovt = array[0] # 选择基准值
        less = [i for i in array[1:] if i <= piovt] # 小于基准值的列表
        greater = [i for i in array[1:] if i > piovt]# 大于基准值的列表
        return quicksort(less) + [piovt] + quicksort(greater)# 递归

print(quicksort(L))
