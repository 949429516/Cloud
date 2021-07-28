"""
狄克斯特拉算法
*不能有负权边
1.找出最便宜的节点
2.计算该最便宜的节点前往各个邻居的开销，并且更新邻居节点
            a
        6        1
start       3        final
        2       5
            b
"""
# 每个节点到邻居的权重
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}
print(graph)
# 每个节点的开销,infinity表示无穷大
infinity = float('inf')
costs = {}
costs['start'] = 0
costs['a'] = infinity
costs['b'] = infinity
costs['fin'] = infinity
print(costs)
# 存储父节点，用来找到最终路径
parents = {}
# parents['a'] = 'start'
# parents['b'] = 'start'
# parents['fin'] = None
# 记录处理过的节点
processed = []


def find_lowest_cost_node(costs):
    """
    找到当前最小开销节点
    :param costs: 字典,存储每个节点开销的字典
    :return: 开销最小的节点
    """
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# 找出未处理的最小开销节点
node = find_lowest_cost_node(costs)
# 循环查找直到所有节点都被处理过则推出循环
while node is not None:
    cost = costs[node] #当前节点的开销
    neighbors = graph[node] #邻居节点字典
    for item in neighbors.keys():
        new_cost = cost + neighbors[item]
        if costs[item] > new_cost:
            costs[item] = new_cost
            parents[item] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(costs)
