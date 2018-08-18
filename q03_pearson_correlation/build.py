# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
def correlation():
    
    coeff=np.corrcoef(dataframe_1['SalePrice'], dataframe_2['SalePrice'])[0,1]
    return float(coeff)

correlation()



