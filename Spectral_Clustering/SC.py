import networkx as nx
import matplotlib.pyplot as plt
import time as t



test=range(1,100)
graph=[]
f = open('p50.txt','r')
for line in f.readlines():
    x,y = line.split()
    graph.append((int(x),int(y)))

G = nx.Graph()
G.add_nodes_from(test)
G.add_edges_from(graph)
#G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35])
#G.add_edges_from([(1,2),(1,3),(2,3),(3,4),(3,10),(5,4),(5,6),(6,7),(5,7),(5,8),(5,9),(8,7),(8,9),(10,11),
                  #(11,12),(13,12),(14,13),(13,15),(14,15),(12,15),(10,16),(16,17),(17,18),(18,19),(19,20),(18,20),(16,21),(22,21),(22,23),(23,24),(24,25),(21,25),(21,24),
                 # (22,24),(16,26),(26,32),(32,33),(33,34),(34,35),(33,35),(26,27),(27,31),(31,28),(28,29),(28,30),(29,30),(29,31),(30,31)])
nx.draw(G)
plt.show()
s=t.time()
G_list=nx.find_cliques(G)
G_real_list=[]
G_clusters=[]
for g1 in G_list:
    G_real_list.append(g1)
print("####################################\n")

G_real_list.sort(key=lambda x:len(x), reverse=True)

G_real_list1=G_real_list[:]


for g1 in G_real_list:
    g=g1[:]
    for g2 in G_real_list:
        if len(set(g1).intersection(g2))>1:
            g+=g2
            G_real_list[G_real_list.index(g2)]=[]
    G_clusters.append(list(set(g)))

G_clusters_top=[]
G_clusters_top1=[]
for elem in G_clusters:
    if len(elem)!=0:
        G_clusters_top.append(elem)

for g1 in G_clusters_top:
    g=g1[:]
    for g2 in G_clusters_top:
        if len(set(g1).intersection(g2))>0:
            g+=g2
            G_clusters_top[G_clusters_top.index(g2)]=[]
    G_clusters_top1.append(list(set(g)))
print("Time:",t.time()-s)
G_clusters_final=[]
for elem in G_clusters_top1:
    if len(elem)!=0:
        G_clusters_final.append(elem)


print('Clusters:',G_clusters_final)
print("####################################\n")





