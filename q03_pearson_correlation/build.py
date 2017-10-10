# Default Imports
import pandas as pd
import numpy as np
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    var1 = dataframe_1['SalePrice']
    var2 = dataframe_2['SalePrice']
    cor = np.corrcoef(var1,var2)
    x = cor[0][1]
    return x
