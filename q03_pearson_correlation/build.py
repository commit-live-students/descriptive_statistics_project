# Default Imports
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def correlation():
    sp_1=dataframe_1.loc[:,'SalePrice']
    sp_2=dataframe_2.loc[:,'SalePrice']
    dataframe_2.head()
    c=np.corrcoef(sp_1,sp_2)[0,1]
    return(float(c))
# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here

c=correlation()
c

