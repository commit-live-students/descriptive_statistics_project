# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    sale = pd.DataFrame(dataframe_1['SalePrice'])
    sale2 = pd.DataFrame(dataframe_2['SalePrice'])
    sale['rank'] = sale['SalePrice'].rank()
    sale2['rank2'] = sale2['SalePrice'].rank()
    df = pd.concat([sale,sale2], axis = 1)
    df['d'] = abs(df['rank'] - df['rank2'])
    df['d squared'] = df['d'] ** 2
    s= df['d squared'].sum()
    n = len(df)
    result = 1- (6*s)/(n*(n**2-1))
    return result



