# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import scipy.stats as stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    s=stats.pearsonr(dataframe_1['SalePrice'],dataframe_2['SalePrice'])
    return s[0]
correlation()


