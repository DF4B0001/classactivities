import pandas as pd
import matplotlib
import numpy as np
data=pd.read_csv("npc_codes.csv")
# print(data)
for x in data:
    if x='NaN':
