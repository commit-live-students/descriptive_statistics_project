# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def correlation():
    sale_price1 = dataframe_1['SalePrice']
    sale_price2 = dataframe_2['SalePrice']
    return sale_price1.corr(sale_price2)


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
