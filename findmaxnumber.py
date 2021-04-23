"""
题目：找出列表中最大数字

思路：分而治之

    基线条件：当列表中只有两个数字时，比较之间的大小

    缩小范围：每次从列表中取出一个数字，直到符合基线条件
"""

L = [2, 3, 6, 8, 10]

def mymax(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        sub_max = mymax(list[1:])
        print(list[0], "--------------", sub_max)
        return list[0] if list[0] > sub_max else sub_max

print(mymax(L))