# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def correlation():
    f1 = dataframe_1['SalePrice']
    f2 = dataframe_2['SalePrice']

    corr = float(format(np.corrcoef(f1,f2)[0][1],'.13f'))
    return corr

correlation()

