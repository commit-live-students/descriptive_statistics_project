# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
sale_price_1 = dataframe_1.loc[:, "SalePrice"]
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
sale_price_2 = dataframe_2.loc[:, "SalePrice"]


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():

    return sale_price_1.corr(sale_price_2)
