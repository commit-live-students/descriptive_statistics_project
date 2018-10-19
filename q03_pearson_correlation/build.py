# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
saleprice1 = dataframe_1.loc[:, 'SalePrice']
saleprice2 = dataframe_2.loc[:, 'SalePrice']

# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    data = np.corrcoef(saleprice1, saleprice2)[0,1]
    return data
correlation()

