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
len("количества строк: " + nodes) # подсчёта количества строк датафреймов
print(nodes(G))

# c( 0 )= 0.3717480344601849
# c( 1 )= 0.601500955007546
# c( 2 )= 0.6015009550075454
# c( 3 )= 0.37174803446018423
