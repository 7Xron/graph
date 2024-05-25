import networkx as nx

G = nx.Graph()

# добавление узлов
G.add_node(0) 
G.add_node(1)
G.add_node(2)

# добавление ребр
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)

print(G)

centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
    print("c(", n, ")=", centrality[n])

# c( 0 )= 0.3717480344601849
# c( 1 )= 0.601500955007546
# c( 2 )= 0.6015009550075454
# c( 3 )= 0.37174803446018423
