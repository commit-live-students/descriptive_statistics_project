# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']
mode_=sale_price.mode()
sale_price=sale_price.values

def calculate_statistics():
    mean_= np.mean(sale_price,dtype=float)
    median_=np.median(sale_price)
    mode1=stats.mode(sale_price,axis=None)
    #print(mean_.dtype)
    #print(median_.dtype)
    mode2=mode1[0]
    return mean_,median_,mode2[0];

#calculate_statistics()
# Return mean,median & mode for the SalePrice Column
# Write your code here




