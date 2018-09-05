# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import scipy.stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    Sales_Price1=pd.Series(dataframe_1['SalePrice'])
    Sales_Price2=pd.Series(dataframe_2['SalePrice'])
    corr= scipy.stats.spearmanr(Sales_Price1,Sales_Price2)[0]
    return corr


spearman_correlation()

