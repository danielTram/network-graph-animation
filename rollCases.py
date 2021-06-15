from numCasesAPI import*
def parse(loc,dateORcase):
    List=[]
    fileobj= open(loc+'.csv','r')
    lineoff=fileobj.readline()
    lines=fileobj.readlines()
    fileobj.close()
    if dateORcase == 'date':
        for ii in lines:
            specimen=ii.strip('\n').split(',')
            List.append(specimen[0])
    else:
        for ii in lines:
            specimen=ii.strip('\n').split(',')
            List.append(specimen[3])
    return List


numCases=[]
dateCases=[]
for ii in district:
    numCases.append(parse(ii,'case'))
    dateCases.append(parse(ii,'date'))
#print(numCases[0])
#print("====="*100)

rollingAverageNumCases=[]
for ii in numCases:
    rollingAverageNumCases.append(rollingAverage(ii,7))
#print(rollingAverageNumCases[0])
#print("====="*50)
print('hello')
print(dateCases[0])
print('='*50)
print(dateCases[1])
for i in range(0,len(dateCases)):
        print(len(dateCases[i]))
print('Start\t'+'Finish')
for i in range(0,len(dateCases)):
	x=dateCases[i]
	print(str(x[0])+'\t'+str(x[len(dateCases[i])-1]))

for i in range(0,len(dateCases)):
	print('printing............')
	print(dateCases[i])
