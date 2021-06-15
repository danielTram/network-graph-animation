import numpy as np
import networkx as nx
#import matplotlib
import matplotlib.pyplot as plt

G=nx.Graph() #constructing graph object
adj=[]
fileObj= open('AdjacencyMatrixUpdate.csv')
line=fileObj.readlines()
fileObj.close()
for ii in line:
    adj.append(ii.split(','))

adjacency=[]
districtNames=[]
for i in adj[1::]: #excludes the column titles
    adjacency.append(i[1:33]) #exludes the row titles and the sum
    districtNames.append(i[0])
#print(districtNames)
    
#print(len(adjacency[0::]))
h=np.array(adjacency,dtype=int)


for ii in range(0,len(h)):
    #G.add_node(str(districtNames[ii]))
    G.add_node(ii)

count1=0
for ii in range(0,len(h)):
    for jj in range(0,len(h)):
        if h[ii,jj]==1:
            count1=count1+1
            G.add_edge(ii,jj)
#print("count1= ",count1)



            

#mapping = dict(zip(G, districtNames))
#G=nx.relabel_nodes(G, mapping)
#nx.draw(G,with_labels=True)


#plt.figure(figsize=(20, 20), dpi=120)
#nx.draw_spectral(G,with_labels=True)
#plt.show()
#nx.draw_networkx_labels(G)
#print(list(G.nodes))
#list(G.edges)

#count=0
#for i in range(0,len(h)):
    #count=int(G.degree[districtNames[i]])+count
    #print("node: "+str(i)+":"+str(districtNames[i])+" has degree of, ",G.degree[districtNames[i]])


#for i in range(0,len(h)):
    #print("node: "+str(i)+":"+str(districtNames[i])+" has neighbours, ",list(G.adj[districtNames[i]]))
            

#count=0
#total=0
#for i in h:
    #for j in i:
        #count=count+j
    #print(count)
    #total=total+count
    #count=0
#print(total)
#extracting adjacency matrix is correct

def transpose(mat, tr, N):
    for i in range(N):
        for j in range(N):
            tr[i][j] = mat[j][i]
   
# Returns true if mat[N][N] is symmetric, else false
def isSymmetric(mat, N):
      
    tr = [ [0 for j in range(len(mat[0])) ] for i in range(len(mat)) ]
    transpose(mat, tr, N)
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != tr[i][j]):
                return False
    return True

#print(isSymmetric(h,len(h)))
#print(np.shape(h))


