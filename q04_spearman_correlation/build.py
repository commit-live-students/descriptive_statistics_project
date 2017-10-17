# Default Import
import pandas as pd
import scipy.stats
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
def spearman_correlation():
    SPr_coef = dataframe_1['SalePrice'].corr(dataframe_2['SalePrice'], method='spearman', min_periods=None)
    return SPr_coef
