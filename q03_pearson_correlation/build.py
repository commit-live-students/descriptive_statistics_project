# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np



# Return the correlation value between the SalePrice column for the two loaded datasets
def correlation():
    dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
    house_price = dataframe_1.loc[:, 'SalePrice']

    dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
    weight_of_nasa_space_shuttle = dataframe_2.loc[:, 'SalePrice']
    return dataframe_1.SalePrice.corr(dataframe_2.SalePrice, method='pearson')

r = correlation()


