"""
广度优先算法
deque双端对列         作为队列使用，队列为先进先出
namedtuple具名元组    取值可命名

        5
    2       6
1       4
    3           8
        7

从1开始找到8并且打印出路径
1.向队列search_deque里添加元素
2.如果该元素是叶子节点,则将其子结点加入到队列search_deque中
3.node为具名元组,name=当前节点,fathername为其父节点
4.
"""
from collections import deque
from collections import namedtuple


def bfs(start_node, end_node, graph):
    """
    :param start_node: 开始节点
    :param end_node: 结束节点
    :param graph: 图
    :return:
    """
    # 定义一个节点，name为当前值，fathername为其父节点记录起源为之后的最短路径存储
    node = namedtuple('node', 'name, fathername')
    # 搜索队列
    search_deque = deque()
    # {'子节点':'父节点'}
    visited = {}
    L = []
    # 向查询队列中添加初始节点
    search_deque.append(node(start_node, None))
    while search_deque:
        """
        1.如果队列中有数据则循环查询
        2.查询当前节点是否在visited中
        3.每次查询则将该节点弹出,并且加入visited中,如果有子结点则将其加入队列
        """
        current_node = search_deque.popleft()
        search_deque_name = current_node.name
        if search_deque_name not in visited:
            # 反向查询路径
            if search_deque_name == end_node:
                L.clear()
                L.append(end_node)
                L.append(current_node.fathername)
                while True:
                    father = visited[L[-1]]
                    if father is None:
                        break
                    L.append(father)
                print(L[::-1])
            else:
                visited[search_deque_name] = current_node.fathername
                for i in graph[search_deque_name]:
                    search_deque.append(node(i, search_deque_name))


if __name__ == "__main__":
    # 使用字典表示有向图
    graph = dict()
    graph[1] = [2, 3]
    graph[2] = [5]
    graph[3] = [4, 7]
    graph[4] = [6]
    graph[5] = [6]
    graph[6] = [8]
    graph[7] = [8]
    graph[8] = []
    print(graph)
    # 执行搜索
    bfs(1, 8, graph)
