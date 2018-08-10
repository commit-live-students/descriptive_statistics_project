# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    sales_price1 = dataframe_1['SalePrice']
    sales_price2 = dataframe_2['SalePrice']
    return sales_price1.corr(sales_price2)



