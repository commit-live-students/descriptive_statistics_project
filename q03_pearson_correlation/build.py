# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


def correlation():
    return dataframe_1['SalePrice'].corr(dataframe_2['SalePrice'])
correlation()
