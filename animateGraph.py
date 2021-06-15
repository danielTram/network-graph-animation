from graphNetwork import G
from rollCases import rollingAverageNumCases, dateCases
from numCasesAPI import district
from DataPls import curRetail,curGrocery,curPark,curTransit,curWorkplace,curResidential,fullDate
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from matplotlib.animation import FuncAnimation,writers
import random
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable
#converts List of rollingAverageNumCases to array form
dateRefine=fullDate[2]
dateUsed=dateRefine[6:]
a=np.array(rollingAverageNumCases)

lengthCases=[]
for i in a:
    lengthCases.append(len(i))
    
b=np.zeros((max(lengthCases),len(district)),dtype=float)
count=-1
for ii in a:
    count+=1
    x=np.array(ii)
    for jj in range(0,len(x)):
        b[jj,count]=x[jj]
#mobility dates go from earliest to latest
b=np.flipud(b) #flip matrix upside down as dates were going from latest to earliest
#fig=plt.figure(figsize=(10, 8), dpi=100)
fig,ax=plt.subplots(figsize=(10,8))
#nx.draw_spectral(G,with_labels=True)
#pos=nx.spring_layout(G,iterations 150)
#fig.subplots_adjust(bottom=0.5)
#updating b to match dates of mobility data 
def sliceB(matrix):
    newMat=matrix[6:,:]
    return newMat
updateB=sliceB(b)

    
colmap = mpl.cm.bwr #seismic
norm = mpl.colors.Normalize(vmin=-100, vmax=100)

fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=colmap),
             orientation='horizontal', label='Mobility % from baseline')
#divider = make_axes_locatable(ax)
#cax = divider.append_axes('right', size='5%', pad=0.05)
#nx.draw_networkx(G,pos)
lab = dict(zip(G, district))
print('printing lab', lab)
leg= dict(zip(range(0,32),district))
textstr = [(str(ii)+': ',district[ii]+'\n')for ii in range(0,len(district))]
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
fig.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

a=np.zeros(len(district),dtype=float)
for ii in range(0, len(district)):
    a[ii]=ii*100
#print(a)

def quadrantPlacement(numNodes):
    pos={}
    random.seed(1)
    q1=0
    q2=0
    q3=0
    q4=0
    for i in range(0, numNodes):
        if (i>=0) and (i<=(0.25*numNodes)): #(-x,y)
            q1=q1+random.randint(0,20)
            x=(random.randint(q1,200+q1))*(-1)
            y=random.randint(q1,200+q1)
            pos.update({i:(x,y)})
        elif (i>=(0.25*numNodes)) and (i<=(0.5*numNodes)):#(x,y)
            q2=q2+random.randint(0,20)
            x=random.randint(q2,200+q2)
            y=random.randint(q2,200+q2)
            pos.update({i:(x,y)})
        elif (i>=(0.5*numNodes)) and (i<=(0.75*numNodes)):#(-x,-y)
            q3=q3+random.randint(0,20)
            x=((random.randint(q3,200+q3)))*(-1)
            y=(random.randint(q3,200+q3))*(-1)
            pos.update({i:(x,y)})
        else: #(x,-y)
            q4=q4+random.randint(0,20)
            x=random.randint(q4,200+q4)
            y=(random.randint(q4,200+q4))*(-1)
            pos.update({i:(x,y)})
        
    return pos

def matrixConverter(List):
    m=np.zeros((len(List[1]),len(district)),dtype=float)
    count=-1
    for i in List:
        count+=1
        c=np.array(i) #turns i list into an array
        for j in range(len(c)):
            m[j,count]=c[j]
    return m

#curTransit,curWorkplace,curResidential
colourRetail= matrixConverter(curRetail)
cGrocery=matrixConverter(curGrocery)
cPark=matrixConverter(curPark)
cTransit=matrixConverter(curTransit)
cWorkplace=matrixConverter(curWorkplace)
cResidential=matrixConverter(curResidential)
#print(colourRetail[:,1])
#ns= b[0,:]*100
#options = {
    #'node_size': ns}
#nodes =nx.draw_networkx_nodes(G,pos) #node_color=c
#plt.show()
#nx.draw_random(G, node_size=b[0,:]*100,with_labels=True)
ns = np.zeros(len(district),dtype=float)
nc = np.zeros(len(district),dtype=float)
#for i in range(0,len(district)):
    #ns[i]=4000
placement=quadrantPlacement(len(district))
initial_size=np.zeros(len(district),dtype=float)
pos=nx.spring_layout(G,pos=placement,k=32,iterations=150)
nodes=nx.draw_networkx_nodes(G,pos,node_size=ns,node_color=nc,cmap=colmap)
nx.draw_networkx_labels(G,pos)
edges=nx.draw_networkx_edges(G,pos)
def update(i):
    ns=b[i,:]*10
    nc= colourRetail[i,:]
    options={'node_size':ns,
         'node_color':nc}
    #nodes=nx.draw_networkx_nodes(G,pos,**options)
    if i>100:
        nodes=nx.draw_networkx_nodes(G,pos,node_size=initial_size)
    else:
        nodes=nx.draw_networkx_nodes(G,pos,**options)
    return nodes,

ss=[]
for i in range(0,len(district)):
    ss.append(str(i)+':'+str(district[i]))
# non ln values
size_coeff=5
m1=plt.scatter([],[],s=10*size_coeff,c='green',alpha=0.7)
m2=plt.scatter([],[],s=100*size_coeff,c='green',alpha=0.7)
m3=plt.scatter([],[],s=200*size_coeff,c='green',alpha=0.7)
m4=plt.scatter([],[],s=300*size_coeff,c='green',alpha=0.7)
m5=plt.scatter([],[],s=400*size_coeff,c='green',alpha=0.7)
legend_m=[m1,m2,m3,m4,m5]
lab= ['10+','100+','200+','300+','400+']
#cityNumber=list(range(0,len(district))
h=[plt.scatter([],[],s=0) for i in range(0,len(district))]

#ln values
lnsize_coeff=300
lnm1=plt.scatter([],[],s=np.log(10)*lnsize_coeff,c='green',alpha=0.7)
lnm2=plt.scatter([],[],s=np.log(100)*lnsize_coeff,c='green',alpha=0.7)
lnm3=plt.scatter([],[],s=np.log(200)*lnsize_coeff,c='green',alpha=0.7)
lnm4=plt.scatter([],[],s=np.log(300)*lnsize_coeff,c='green',alpha=0.7)
lnm5=plt.scatter([],[],s=np.log(400)*lnsize_coeff,c='green',alpha=0.7)
lnlegend_m=[lnm1,lnm2,lnm3,lnm4,lnm5]
lnlab= ['10+','100+','200+','300+','400+']
#cityNumber=list(range(0,len(district))
lnh=[plt.scatter([],[],s=0) for i in range(0,len(district))]        
def animate(i):
    fig.clear()
    ax.clear()
    ns=updateB[i,:]*5
    nc=cGrocery[i,:]
    #nc=colourRetail[i,:]
    #nc=cPark[i,:]
    #nc=cTransit[i,:]
    #nc=cWorkplace[i,:]
    #nc=cResidential[i,:]
    nodes=nx.draw_networkx_nodes(G,pos,node_size=ns,node_color=nc,cmap=colmap)
    edges=nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos)
    fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=colmap),
             orientation='horizontal', label='Mobility % from baseline')
    fig.suptitle("Day:   "+str(i+1)+'\nDate:  '+str(dateUsed[i]), fontweight="bold")
    fig.legend(handles=legend_m,labels=lab,ncol=5,loc=(0.25,0.25))
    fig.legend(handles=h,labels=ss,loc='upper left',fontsize='xx-small')
    #ax.text(-1, 1,ss,transform=ax.transAxes, fontsize=7)
        
#lnb=np.log(updateB)
def logUpdateB(mat):
    for i in range(0,len(updateB[:,0])): #looping through rows
        for j in range(0,len(updateB[0,:])): #looping through columns
            if mat[i,j] != 0:
                mat[i,j]=np.log(mat[i,j])
    return mat
lnUpdateB=logUpdateB(updateB)
    
def animateLn(i):
    fig.clear()
    ax.clear()
    ns=lnUpdateB[i,:]*300
    #nc=colourRetail[i,:]
    #nc=cGrocery[i,:]
    #nc=cPark[i,:]
    #nc=cTransit[i,:]
    nc=cWorkplace[i,:]
    #nc=cResidential[i,:]
    nodes=nx.draw_networkx_nodes(G,pos,node_size=ns,node_color=nc,cmap=colmap)
    edges=nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos)
    fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=colmap),
             orientation='horizontal', label='Mobility % from baseline')
    fig.suptitle("Day:   "+str(i+1)+'\nDate:  '+str(dateUsed[i]), fontweight="bold")
    fig.legend(handles=lnlegend_m,labels=lab,ncol=5,loc=(0.25,0.25))
    fig.legend(handles=lnh,labels=ss,loc='upper left',fontsize='xx-small')  
#fig.legend(labels=district,ncol=len(district),loc='upper left')
anim=FuncAnimation(fig,animateLn,frames=len(dateUsed),interval=300,repeat=False)
#Writer=writers['ffmpeg']
#writer=Writer(fps=3,metadata={'artist':'Me'},bitrate=3000)
#anim.save('1_Residential.mp4',writer)
plt.show()
