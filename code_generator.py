# {id: 1, group:'cl1', label: 'Node 1'},
# {id: 2, group:'cl1', label: 'Node 2'},
# {id: 3, group:'cl1', label: 'Node 3'},
# {id: 4, group:'cl2', label: 'Node 4'},
# {id: 5, group:'cl2', label: 'Node 5'}
#
# {from: 1, to: 3},
# {from: 1, to: 2},
# {from: 2, to: 4},
# {from: 2, to: 5}

def get_graph(file):
    g = {}
    f = open(file,'r')
    for line in f.readlines():
        x,y = line.split()
        if x in g.keys():
            g[x].add(y)
        else:
            g.update({x: set(y)})
        if y in g.keys():
            g[y].add(x)
        else:
            g.update({y: set(x)})
    return g

def get_edges_code(graph, file):
    f = open(file,'w')
    str = ''
    unique = []
    for node in graph.keys():
        for edge in graph[node]:
            if ((node,edge) not in unique) and ((edge,node) not in unique):
                str += '{from: %s, to: %s},\n' % (node, edge)
                unique.append((node,edge))
    f.write(str)
    f.close()

def get_nodes_code(graph, clusters, algo, file):
    f = open(file,'w')
    str = ''
    for node in graph.keys():
        for indx in range(len(clusters)):
            if algo == 'MCL':
                node = int(node)
            if node in clusters[indx]:
                str += "{id: %s, group:'cl%s', label: '%s'},\n" % (node, indx+1, node)
    f.write(str)
    f.close()

graph = get_graph('p30.txt')
print(graph)

clique_cl = [[28, 29, 30, 31],[1, 2, 3, 4],[5, 6, 7, 8, 9],[12, 13, 14, 15],[18, 19, 20],[21, 22, 23, 24, 25],[33, 34, 35],[16, 17, 10, 11],[32, 26, 27]]

get_edges_code(graph, 'CL30_edges.txt')
get_nodes_code(graph, clique_cl, 'MCL', 'CL30_nodes.txt')