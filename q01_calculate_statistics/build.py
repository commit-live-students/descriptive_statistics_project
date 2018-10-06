# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics(): 
    data = pd.read_csv('data/house_prices_multivariate.csv')
    sale_price = data.loc[:, 'SalePrice']
    sale_price1 = np.array(sale_price)
#    mode1 = pd.Series(sale_price1.argmax(axis=0))
    mode1 = np.array(sale_price.mode()).astype(int)[0]
    
    return (np.mean(sale_price),np.median(sale_price),mode1)
calculate_statistics()


