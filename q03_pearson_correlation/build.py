# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    pc1 = dataframe_1.loc[ :, 'SalePrice']
    pc2 = dataframe_2.loc[ :, 'SalePrice']
    return float(np.corrcoef(pc1, pc2)[0, 1])


