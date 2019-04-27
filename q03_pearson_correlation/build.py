# Default Imports
import numpy as np
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    sale_price1 = dataframe_1.loc[:, 'SalePrice']
    sale_price2 = dataframe_2.loc[:, 'SalePrice']
    correlate = np.corrcoef(sale_price1, sale_price2)[0,1]
    return correlate
