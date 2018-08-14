# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
from scipy.stats import spearmanr

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
def spearman_correlation():
    saleprice = dataframe_1.loc[:,'SalePrice']
    saleprice2 = dataframe_2.loc[:,'SalePrice']
    coef, p = spearmanr(saleprice, saleprice2)
    return coef




