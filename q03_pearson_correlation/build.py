# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
def correlation():
    sale_price1 = dataframe_1['SalePrice']
    sale_price2 = dataframe_2['SalePrice']
    pcc = pd.Series.corr(sale_price1, sale_price2)
    return pcc

correlation()
