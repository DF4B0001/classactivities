import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('data.csv')
df.boxplot()
plt.show()