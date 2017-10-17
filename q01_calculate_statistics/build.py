# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]
def calculate_statistics():
    mean = sale_price.mean()
    #print(mean)
    median = sale_price.median()
    #print(median)
    mode = sale_price.mode()
   # print(mode)
    return mean,median,mode.values[0]



# Return mean,median & mode for the SalePrice Column
# Write your code here
