import numpy as np
import time
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


# Matrix operations ###

def print_matr(matr):
    for row in matr:
        print(row)

def power(matr, p):
    return np.linalg.matrix_power(matr, p)

def inflation(matr, r):
    for col_indx in range(len(matr)):
        col = normalize_col(power_col(get_col(matr,col_indx),r))
        matr = set_col(matr, col_indx, col)
    return matr

def equal(matr1, matr2):
    eq = True
    for row in range(len(matr1)):
        for col in range(len(matr1)):
            if matr1[row][col] != matr2[row][col]:
                eq = False
    return eq

#######################

# Column operations ###

def get_col(matr,i):
    col = []
    for row in range(len(matr)):
        col.append(matr[row][i])
    return col

def normalize_col(col):
    s = sum(col)
    for elem in range(len(col)):
        col[elem] = col[elem]/s
    return col

def power_col(col,r):
    return np.power(col,r)

def set_col(matr,i, col):
    for row in range(len(matr)):
        matr[row][i] = col[row]
    return matr

#######################
def adjacency_matrix(g):
    n = len(g.keys())
    matr = [[0 for i in range(n)] for i in range(n)]
    row = 0
    for node in g.keys():
        for neighbour in g[node]:
            matr[row][int(neighbour)-1] = 1
        row += 1
    return matr

def add_self_loop(matr):
    for i in range(len(matr)):
        matr[i][i] = 1
    return matr

def normalize(matr):
    for col_indx in range(len(matr)):
        col = normalize_col(get_col(matr,col_indx))
        matr = set_col(matr,col_indx,col)
    return matr


def MCL(graph, expand_power=2, inflation_power=2, self_loop=True):
    M = adjacency_matrix(graph)
    if self_loop == True:
       M = add_self_loop(M)
    M = normalize(M)
    step = 0
    while(True):
        print('iter')
        old_M = M
        M = inflation(power(M,expand_power),inflation_power)
        step += 1
        if equal(M,old_M):
            print('Stop step #', step)
            break
    return M

def generate_clusters(m):
    clusters = []
    for row in m:
        if any(row):
            clust_elem = []
            for indx in range(len(row)):
                if row[indx]:
                    clust_elem.append(indx+1)
            clusters.append(clust_elem)
    unique = []
    del_indx = []
    for indx in range(len(clusters)):
        for elem in clusters[indx]:
            if elem in unique:
                del_indx.append(indx)
                break
            else:
                unique.append(elem)
    for ind in del_indx:
        clusters.pop(ind)
    return clusters


graph = get_graph('p100.txt')
print(len(list(graph.keys())))

s = time.time()

x = MCL(graph, 2, 2)

print(time.time() - s)

clusts = generate_clusters(x)

print(len(clusts))
#print(clusts)

#code_generator.get_edges_code(graph, 'MCL20_edges.txt')
#code_generator.get_nodes_code(graph,clusts, 'MCL', 'MCL20_nodes.txt')



