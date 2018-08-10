# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    sales1 = dataframe_1['SalePrice']
    sales2 = dataframe_2['SalePrice']
    return sales1.corr(sales2, method='spearman')




