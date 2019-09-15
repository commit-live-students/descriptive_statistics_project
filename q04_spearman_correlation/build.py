# Default Import
import pandas as pd
import numpy as np
from scipy import stats
from scipy import stats
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    data1 = dataframe_1.loc[:,'SalePrice']
    data2 = dataframe_2.loc[:,'SalePrice']
    spearmancoeff = stats.spearmanr(data1,data2)
    return spearmancoeff[0]
print spearman_correlation()
