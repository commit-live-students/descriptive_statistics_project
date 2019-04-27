# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    coefficient = dataframe_1['SalePrice'].corr(dataframe_2['SalePrice'], method = 'spearman')
    return coefficient

spearman_correlation()
