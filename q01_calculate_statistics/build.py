# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
df=data
sale_price = df.loc[:, 'SalePrice']

def  calculate_statistics():
    a=sale_price.mean()
    b=sale_price.median()
    c=sale_price.mode()[0]
    return a,b,c
 
    
    
    
# Return mean,median & mode for the SalePrice Column
# Write your code here


c=calculate_statistics()
c


