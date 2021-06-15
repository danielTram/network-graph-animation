import numpy as np

fileobj = open('2020_GB_Region_Mobility_Report.csv','r')
lineoff=fileobj.readline()
lines=fileobj.readlines()
#print('size: ', len(lines))
fileobj.close()

countrys=[]
states=[]  # greater london
cities=[] # 
dates=[]  #required
retails=[] #
grocerys=[] #
parks=[] #
transits=[] #
workplaces=[] #
residentials=[] #

#extracts columns
for i in lines:
    data=i.split(',') #splits each column into respective category
    countrys.append(data[1])
    states.append(data[2])
    cities.append(data[3].strip(' ').strip('"')) #Takes away white spaces and apostrophees
    dates.append(data[8]) #can do .split('-') to get rid of hyphen 
    retails.append(data[9])
    grocerys.append(data[10])
    parks.append(data[11])
    transits.append(data[12])
    workplaces.append(data[13])
    residentials.append(data[14].strip('\n'))
 #year-month-day


def printPlaces(place):
    for i in place:
        if i !='':
            print(i)

#printPlaces(state)
#noun=str(input('What city would you like to analyse? '))
def indexPlace(place):
    count=0
    index=[]
    for i in place:
        count=count+1
        if i == 'Greater London': #noun
            index.append(count-1)#-1 to account for 0 indexing
    return index
y=indexPlace(states)
#print(y)

low=min(y)
high=max(y)

city=cities[low:high]
date= dates[low:high]  #required
retail=retails[low:high] #
grocery=grocerys[low:high] #
park=parks[low:high] #
transit=transits[low:high] #
workplace=workplaces[low:high] #
residential=residentials[low:high]
    
#print(low)
#print(high)
x=city
#print(len(x[395:788]))

#////////////
unique=[] #cities within greater london
for i in x:
    if i not in unique:
        unique.append(i)

#print(unique)
#print(len(unique))
val= np.zeros((len(x),len(unique)),dtype=object)
#print(len(val))
count=0
#for i in range(0, len(unique)):
for i in range(0,len(x)):
    for j in range(0,len(unique)):
        if x[i] == unique[j]:
            count=count+1
            val[i,j]=count
    

#print(val[:,0])
#print(np.shape(val))
#print(val[1:])

req=np.zeros((len(unique),2),dtype=object)

for i in range(0,len(val[0,:])): #number of columns
    req[i,0]=np.min(val[:,i][np.nonzero(val[:,i])])
    req[i,1]=max(val[:,i])
#print(req)
#print(len(req[:,0]))
#print(len(date[req[0,0]:req[0,1]]))
#len(req[:,0])
#print((x[2758:3153]))

#///////////
fullDate=[]
fullRetail=[]
fullGrocery=[]
fullPark=[]
fullTransit=[]
fullWorkplace=[]
fullResidential=[]
for j in range(0, len(req[:,0])):
    b=date[req[j,0]-1:req[j,1]]
    c=retail[req[j,0]-1:req[j,1]]
    d=grocery[req[j,0]-1:req[j,1]]
    e=park[req[j,0]-1:req[j,1]]
    f=transit[req[j,0]-1:req[j,1]]
    g=workplace[req[j,0]-1:req[j,1]]
    h=residential[req[j,0]-1:req[j,1]]
    fullDate.append(b)
    fullRetail.append(c)
    fullGrocery.append(d)
    fullPark.append(e)
    fullTransit.append(f)
    fullWorkplace.append(g)
    fullResidential.append(h)
#print((fullDate))
#print(unique)
#print(fullDate[33])
#print(len(unique))
#print(fullRetail[1])
#print(len(fullRetail[1]))


#print(unique[0:3])

def rollingAverage(List,n): #
    rollAverage=[]
    count=0
    integerList=[]
    for i in List: #converts to to integer
        if i =='': #NA values converted to 0
            integerList.append(int(0))
        else:
            integerList.append(int(i))
    while count<(len(List)-n+1):
        rollSize=integerList[count:count+n]
        dataPoint=sum(rollSize)/n
        rollAverage.append(dataPoint)
        count+=1
    return rollAverage



        
#print(rollingAverage(fullRetail[1],7))    

rollRetail=[]
rollGrocery=[]
rollPark=[]
rollTransit=[]
rollWorkplace=[]
rollResidential=[]
for ii in range(0, len(unique)):
    rollRetail.append(rollingAverage(fullRetail[ii],7))
    rollGrocery.append(rollingAverage(fullGrocery[ii],7))
    rollPark.append(rollingAverage(fullPark[ii],7))
    rollTransit.append(rollingAverage(fullTransit[ii],7))
    rollWorkplace.append(rollingAverage(fullWorkplace[ii],7))
    rollResidential.append(rollingAverage(fullResidential[ii],7))
#print(len(rollRetail))

def combineLondonAndHackney(List):
	ll=[]
	London=List[1]
	Hackney=List[12]
	List.remove(List[1])#london
	List.remove(List[12])#hackney
	List.remove(List[0])#greater london
	for i in range(0, len(London)):
		LondonAndHackney=(London[i]+Hackney[i])/2
		ll.append(LondonAndHackney)
	List.insert(0,ll)
	return List
curRetail=combineLondonAndHackney(rollRetail)
curGrocery=combineLondonAndHackney(rollGrocery)
curPark=combineLondonAndHackney(rollPark)
curTransit=combineLondonAndHackney(rollTransit)
curWorkplace=combineLondonAndHackney(rollWorkplace)
curResidential=combineLondonAndHackney(rollResidential)

testArray=np.array(curRetail[1])
#print(len(testArray))
#print(np.shape(testArray))
#print(len(curRetail[1]))
print(len(fullDate))
for i in range(0,len(fullDate)):
	print(len(fullDate[i]))
#	if fullDate[i]==fullDate[i+1]:
#		print('True')
print(fullDate[2])	
