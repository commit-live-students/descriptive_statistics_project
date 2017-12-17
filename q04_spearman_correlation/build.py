# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    return pd.concat((dataframe_1['SalePrice'], dataframe_2['SalePrice']), axis=1, join='inner').corr(method='spearman').iloc[0,1]
