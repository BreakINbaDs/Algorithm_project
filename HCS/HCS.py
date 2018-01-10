import random
import time
import karger
import code_generator

def get_graph(file):
    g = {}
    f = open(file,'r')
    for line in f.readlines():
        x,y = line.split()
        if x in g.keys():
            if y not in g[x]:
                g[x].append(y)
        else:
            g.update({x: [y]})
        if y in g.keys():
            if x not in g[y]:
                g[y].append(x)
        else:
            g.update({y: [x]})
    return g


def min_cut(graph):
    data = [[[node], graph[node]] for node in graph.keys()]
    graph = [karger.Adjacency(i[0], i[1]) for i in data]
    cuts = []
    for i in range(10):
        cuts.append(karger.min_cut(graph))
    diff = 10
    chosen = 0
    for indx in range(len(cuts)):
        c = extract_cut(cuts[indx])
        d = abs(len(c[0]) - len(c[1]))
        if d < diff:
            diff = d
            chosen = indx
    return extract_cut(cuts[chosen])

def extract_cut(cut):
    nodes1 = cut[0][0].node
    nodes2 = cut[0][1].node
    return (nodes1, nodes2)

def check_conectivity(nodes1, nodes2, graph):
    if len(nodes1) == 1 or len(nodes2) == 1:
        return True
    if len(nodes1) <= len(nodes2):
        num = 0
        for node in nodes1:
            for neighbour in nodes2:
                if neighbour in graph[node]:
                    num += 1
    else:
        num = 0
        for node in nodes2:
            for neighbour in nodes1:
                if neighbour in graph[node]:
                    num += 1
    if num > len(graph.keys())/2:
        return True
    else:
        return False

def subgraph(graph,nodes):
    subg = {}
    for node in nodes:
        subg.update({node: [x for x in graph[node] if x in nodes]})
    return subg

HCS_clusters = []
def HCS(graph):
    n_nodes = len(list(graph.keys()))
    cuts = min_cut(graph)
    print('min cut done')
    if check_conectivity(cuts[0],cuts[1],graph):
        HCS_clusters.append(cuts[0]+cuts[1])
    else:
        print('level')
        HCS(subgraph(graph, cuts[0]))
        HCS(subgraph(graph, cuts[1]))

graph = get_graph('p100.txt')

s=time.time()
HCS(graph)
print(time.time()-s)
#print(HCS_clusters)
#code_generator.get_edges_code(graph, 'HCS20_edges2.txt')
#code_generator.get_nodes_code(graph,HCS_clusters, 'HCS', 'HCS20_nodes2.txt')