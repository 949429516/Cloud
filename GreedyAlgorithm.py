"""
贪婪算法

尽可能少的电台覆盖所有的州
states_needed:所有州的集合
stations:电台清单字典，键为电台，值为该电台覆盖的州集合类型
"""
# 集合去重复{}，需要覆盖的洲
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
# 电台清单
stations = {}
stations['kone'] = {'id', 'nv', 'ut'}
stations['ktwo'] = {'wa', 'id', 'mt'}
stations['kthree'] = {'or', 'nv', 'ca'}
stations['kfour'] = {'nv', 'ut'}
stations['kfive'] = {'ca', 'az'}
# 存储最终的广播电台集合
final_stations = set()

while states_needed:
    """
    如果states_needed为空退出循环，说明所有的州均被覆盖
    1.每次挑选出覆盖最多州的电台（每次找到最优解,每次找到的电台尽可能多的覆盖需要的州）
    2.将每次循环中覆盖最多州的电台添加到final_stations中
    3.删除states_needed中已经覆盖的电台
    """
    # 存储覆盖最多州的电台
    best_station = None
    # 存储本次循环找到的电台所覆盖州的集合
    states_covered = set()
    # 遍历电台清单，station=电台，states=电台覆盖的州
    for station, states in stations.items():
        # 该电台覆盖的州和需要覆盖的州取交集
        covered = states & states_needed
        if len(covered) > len(states_covered):
            # 通过长度判断覆盖最多的州
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_needed -= states_covered

print(final_stations)