# Default Import
import pandas as pd
from scipy.stats import spearmanr

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    spr_coef= spearmanr(dataframe_1['SalePrice'],dataframe_2['SalePrice'])
    return spr_coef[0]
