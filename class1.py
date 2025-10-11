import pandas as pd
import matplotlib as plt
import numpy as np
from pandas.core.interchange.dataframe_protocol import DataFrame
data=pd.read_csv("npc_codes.csv")
# delete all rows and columns with NaN
data.dropna(axis=0,how='all',inplace=True)
data.dropna(axis=1,how='all',inplace=True)
data.drop(data.columns[-1],axis=1,inplace=True)
data.drop(data.columns[0],axis=1,inplace=True) #remove NaN in the last row
data = data.dropna(how='any') #remove the NaN in the bottom right hand corner
print(data) #cleaning data
