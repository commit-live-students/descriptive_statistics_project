# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd
data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    return  sale_price.mean(),sale_price.median(),np.array(sale_price.mode())[0]



