# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
from scipy.stats import spearmanr
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
saleprice1 = dataframe_1.loc[:, 'SalePrice']
saleprice2 = dataframe_2.loc[:, 'SalePrice']
# Your code here
def spearman_correlation():
    df = pd.concat([saleprice1,saleprice2], axis=1).corr(method='spearman').iloc[0,-1]
#     corr = spearmanr(saleprice1, saleprice2)
    return df
spearman_correlation()


