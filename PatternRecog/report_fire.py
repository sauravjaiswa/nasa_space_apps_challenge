# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 23:08:14 2019

@author: mr_ro
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:52:45 2019

@author: mr_ro
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2, whiten
import math
import requests

os.chdir("C:/Users/mr_ro/Documents/GitHub/nasa_space_apps_challenge/PatternRecog")
url='https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_USA_contiguous_and_Hawaii_24h.csv'
response = requests.get(url)
with open(os.path.join("downloaded_data.csv"), 'wb') as f:
    f.write(response.content)
    
df = pd.read_csv("downloaded_data.csv")    
coordinates = np.array(df.loc[:,"latitude":"longitude"])
"""
def funcUserData():
    userLat = float(input("Enter the latitude"))
    userLong = float(input("Enter the Longitude"))
    userMonth = float(input("Enter the Month"))
    
    userDataList = [userLat,userLong,userMonth]
    return userDataList
"""


def funcFindCoords(userDataList):
    areaList = []
    distRad = 3
    userCoord = userDataList[0:2]
    distTemp = 0
    for i in range(0,len(coordinates)):
        latTemp = coordinates[i][0]
        longTemp = coordinates[i][1]
        distTemp = 111*math.sqrt(((latTemp - userCoord[0])**2) + ((longTemp - userCoord[1])**2))
        if distTemp <= distRad:
            areaList.append([i,coordinates[i][0],coordinates[i][1],distTemp])
            
    
    return areaList
                


"""
#calling part of the code
for j in range(0,500):
    
    userDataList =  [indiaCSV.loc[j,"latitude"],indiaCSV.loc[j,"longitude"],indiaCSV.loc[j,"months"]]     #funcUserData()
    areaList = funcFindCoords(userDataList)
    #print(areaList)
    
    indexList = []
    for i  in areaList:
        indexList.append(i[0])
    
    prob = funcFindProb(indexList,userDataList)
    print("index ",j,": Prob = ",prob*100," %")

"""

userDataList = [34.328,-118.545,10]     #funcUserData()
areaList = funcFindCoords(userDataList)
#print(areaList)
indexList = []
for i  in areaList:
    indexList.append(i[0])

coordDF = pd.DataFrame(areaList)
coordDF.to_csv("area.csv",index = False)











    

    
