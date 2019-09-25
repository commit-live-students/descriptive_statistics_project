# Default Imports
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
def correlation():

    dataframe_1_SalePrice = dataframe_1.loc[:, 'SalePrice']
    dataframe_2_SalePrice = dataframe_2.loc[:, 'SalePrice']
    correlation_coefficient = np.corrcoef(dataframe_1_SalePrice, dataframe_2_SalePrice)[1][0]

    return correlation_coefficient
