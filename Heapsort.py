"""
堆排序
第一个叶子节点的下标：len(L)//2-1
叶子节点第一个子结点：下标*2 + 1
叶子节点第二个子结点：下标*2 + 2
"""

L = [2, 1, 3, 9, 7, 4, 6, 5, 8]


def createHeap(L):
    # 列表的最大下标
    max_subscript = len(L) - 1
    first_Leaf_node = len(L) // 2 - 1
    leftchildnode = first_Leaf_node * 2 + 1
    rightchildnode = first_Leaf_node * 2 + 2
    while first_Leaf_node >= 0:
        L = up_move(L, max_subscript, first_Leaf_node, leftchildnode, rightchildnode)
        first_Leaf_node -= 1
        leftchildnode = first_Leaf_node * 2 + 1
        rightchildnode = first_Leaf_node * 2 + 2
    return L


def up_move(L, max_subscript, first_Leaf_node, leftchildnode, rightchildnode):
    if rightchildnode <= max_subscript:
        if L[first_Leaf_node] > L[leftchildnode]:
            L[first_Leaf_node], L[leftchildnode] = L[leftchildnode], L[first_Leaf_node]
        if L[first_Leaf_node] > L[rightchildnode]:
            L[first_Leaf_node], L[rightchildnode] = L[rightchildnode], L[first_Leaf_node]
        if L[leftchildnode] > L[rightchildnode]:
            L[leftchildnode], L[rightchildnode] = L[rightchildnode], L[leftchildnode]
    else:
        if L[first_Leaf_node] > L[leftchildnode]:
            L[first_Leaf_node], L[leftchildnode] = L[leftchildnode], L[first_Leaf_node]
    return L


def start(L):
    L = createHeap(L)
    arr = []
    for i in range(len(L)):
        L[0], L[-1] = L[-1], L[0]
        arr.append(L.pop(-1))
        createHeap(L)
    print(arr)

start(L)