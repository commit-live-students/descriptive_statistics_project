# Default Imports
import pandas as pd
import numpy as np
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    x=dataframe_1['SalePrice']
    y=dataframe_2['SalePrice']
    p_corr=np.corrcoef(x,y)[0,1]
    return p_corr
