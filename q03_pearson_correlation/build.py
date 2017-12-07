# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
import numpy as np
def correlation():
    return np.corrcoef(dataframe_1['SalePrice'], dataframe_2['SalePrice'])[0,1]

#print correlation()
