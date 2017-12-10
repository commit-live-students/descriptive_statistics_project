# Default Import
import pandas as pd
import numpy as np
from scipy import stats
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    sp_1=dataframe_1.loc[:, "SalePrice"]
    sp_2=dataframe_2.loc[:, "SalePrice"]
    r=stats.spearmanr(sp_1,sp_2)
    return float(r[0])
