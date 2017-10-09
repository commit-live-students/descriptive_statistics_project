# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
house_price = dataframe_1.loc[:, 'SalePrice']

dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
weight_of_nasa_space_shuttle = dataframe_2.loc[:, 'SalePrice']


def spearman_correlation():
    # Enter code here


