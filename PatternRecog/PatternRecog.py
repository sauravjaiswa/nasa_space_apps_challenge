# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:52:45 2019

@author: mr_ro
"""

import os
import pandas as pd
import math

os.chdir("C:/Users/mr_ro/Desktop/NASA")
indiaCSV = pd.read_csv("india_copy.csv")
"""
defining the coordinate which we are going to use as reference
"""
row = 0
latRef =0# indiaCSV.loc[row,"latitude"]	
longRef =0# indiaCSV.loc[row,"longitude"]

"""
xDiff = yDiff = 0.0
xList = indiaCSV.loc[:,"latitude"]
yList = indiaCSV.loc[:,"longitude"]
coordList = indiaCSV.loc[:,"latitude":"longitude"]
print("READY")

i = 0
latTemp = longTemp = 0
distTemp = 0
distMin = 1000
indexMin = 0
for i in range(1,len(coordList)) : 
    latTemp = coordList.loc[i,"latitude"]
    #longTemp = coordList.loc[i,"longitude"]
    xDiff = (latRef - latTemp)**2
    #yDiff = (longRef - longTemp)**2
    distTemp = xDiff
    if distTemp <= distMin:
        print(distTemp," ", i)
        indexMin = i
        distMin = distTemp

print(indexMin)
"""
"""
new method
"""
distRad = math.sqrt(0.0019)
print("distRad",distRad)
xDiff = yDiff = 0.0
xList = indiaCSV.loc[:,"latitude"]
yList = indiaCSV.loc[:,"longitude"]
coordList = indiaCSV.loc[:,"latitude":"longitude"]

i = 0
j = 0
latTemp = longTemp = 0
distTemp = 0
df = pd.DataFrame({"latitude":[], "longitude":[]}) 
for i in range(0,50):
    row = i
    latRef = indiaCSV.loc[row,"latitude"]	
    longRef = indiaCSV.loc[row,"longitude"]
    print("REF COORD: INDEX ",i," = ",latRef," ",longRef)
    print("")
    #missing here
    """
    if i!=0:
        emptyDict = {'latitude': [-1], 'longitude': [-1]}
        indexDf = pd.DataFrame(emptyDict)
        df = df.append(indexDf)
    """ 
    df = df.append(pd.DataFrame({"latitude":[0000], "longitude":[0000]}) )
    indexDict = {'latitude': [latRef] , 'longitude': [longRef]}
    indexDf = pd.DataFrame(indexDict)
    df = df.append(indexDf)
    
    
    
    
    for j in range(0,500) : 
        if j!=i:
            latTemp = coordList.loc[j,"latitude"]
            longTemp = coordList.loc[j,"longitude"]
            xDiff = (latRef - latTemp)**2
            yDiff = (longRef - longTemp)**2
            distTemp = math.sqrt(xDiff+yDiff)
            if distTemp <= distRad:
                print(coordList.iloc[j,:])
                series = coordList.iloc[j,:]
                #print(type(series))
                df = df.append(series) # appending in temp dataframe
                print(" ")
    print("DONE")
    print("")
    #df = df.append(pd.DataFrame({"latitude":[], "longitude":[]}) )
    df = df.append(pd.DataFrame({"latitude":[0000], "longitude":[0000]}) )

name = str("INDEX.csv")
df.to_csv(name)
"""
creating dataframe
"""








    

    
