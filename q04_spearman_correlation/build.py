# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
from scipy.stats import spearmanr
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    df1 = dataframe_1.loc[:, 'SalePrice']
    df2 = dataframe_2.loc[:, 'SalePrice']
    corr, p_value = spearmanr(df1, df2)
    print(corr)
    return corr
spearman_correlation()



