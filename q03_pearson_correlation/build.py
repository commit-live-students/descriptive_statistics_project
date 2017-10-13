# Default Imports
import pandas as pd
import numpy as np
#import scipy as sc
def correlation() :

    dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
    x = dataframe_1['SalePrice']
    dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
    y = dataframe_2['SalePrice']
    r = np.corrcoef(x, y)
    #r = sc.stats.pearsonr(x, y)

    return r[0,1]
# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
