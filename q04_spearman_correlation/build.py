# Default Import
import pandas as pd
from pandas import DataFrame

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():

    dataframe_1_SalePrice = dataframe_1.loc[:, 'SalePrice']
    dataframe_2_SalePrice = dataframe_2.loc[:, 'SalePrice']

    # Computing rank
    rank1 = dataframe_1_SalePrice.rank(ascending = True)
    rank2 = dataframe_2_SalePrice.rank(ascending = True)

    spearman = DataFrame()
    spearman['d'] = rank1 - rank2
    spearman['d-squared'] = spearman['d'] ** 2
    d_squared_sum = spearman['d-squared'].sum()
    n = dataframe_1_SalePrice.shape[0]

    # Formula for calculating Spearman correlation coefficient
    spearman_corr_coeff = 1 - (6 * d_squared_sum / (n * (n ** 2 - 1)))

    return spearman_corr_coeff
