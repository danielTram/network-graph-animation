#data extraction of infected cases
#using API
from DataPls import*
from uk_covid19 import Cov19API

#filters
def caseExtract(loc):
    england_only=[
        'areaType=ltla',
        'areaName='+str(loc)
    ]


    #structure
    newAndCumaCases={
        "date":"date",
        "areaName":"areaName",
        "cumCasesBySpecimenDate":"cumCasesBySpecimenDate",
        "newCasesBySpecimenDate":"newCasesBySpecimenDate"

    }
    #now we create the object
    api = Cov19API(filters=england_only,structure=newAndCumaCases)
    data=api.get_csv()
    output= open(loc+'.csv','w')
    output.write(data)
    output.close()

s=[]
t=[]
c=[]
for ii in unique:
    c.append(ii.split('City of '))
    s.append(ii.split('Royal Borough of '))
    t.append(ii.split('London Borough of '))




district=[]
def cityNames(d, f):
    for ii in d:
        if len(ii) == 2:
            f.append(ii[1])

cityNames(c,district)
cityNames(t,district)
cityNames(s,district)
#print(district)
#print(len(district))


#for ii in district:
    #caseExtract(str(ii))
district.remove('London')
district.remove('Hackney')
district.insert(0,'Hackney and city of London')
#print(district)

#This code below creates csv files for all the cities in greater london.Hashtagged out to prevent from redoing this all the time
#for ii in district:
    #caseExtract(str(ii))


