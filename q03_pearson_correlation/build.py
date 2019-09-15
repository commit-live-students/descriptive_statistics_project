# Default Imports
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    data1 = dataframe_1.loc[:,'SalePrice']
    data2 = dataframe_2.loc[:,'SalePrice']
    return np.corrcoef(data1,data2)[0,1]
print correlation()
