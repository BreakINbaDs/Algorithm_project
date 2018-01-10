import networkx as nx

def get_graph(file):
    g = nx.Graph()
    f = open(file,'r')
    for line in f.readlines():
        x,y = line.split()
        g.add_edge(x,y)
    return g

g = get_graph('graph.txt')

print(nx.clustering(g))