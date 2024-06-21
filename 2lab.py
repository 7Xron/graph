import networkx as nx
G = nx.Graph() # Создаем пустой неориентированный граф
# Добавляем вершины
G.add_nodes_from([1, 2, 3, 4])
# добавление ребр
G.add_nodes_from(1, 2)
G.add_nodes_from(1, 3)
G.add_nodes_from(1, 4)
print(G) # выводим вершины и ребра

def nodes(G):
    sc = nx.closeness_centrality(G) # создаем словарь центральностей
    dadaf = pd.DataFrame.from_dict({'вершина': list(sc.keys()), 'центральность': list(sc.values())}) # вывод словаря в датафрейм
    return dadaf.sort_values('центральность', ascending=False)# возвращаем список центральностей, сортируем по убываниию
print(nodes(G))

Graph with 4 nodes and 3 edges
   вершина  центральность
0        1            1.0
1        2            0.6
2        3            0.6
3        4            0.6
