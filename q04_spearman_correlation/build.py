# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    sales_price1 = dataframe_1['SalePrice']
    sales_price2 = dataframe_2['SalePrice']
    return sales_price1.corr(sales_price2, method = 'spearman')
