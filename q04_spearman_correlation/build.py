# Default Import
import pandas as pd
import scipy.stats as s

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    return s.spearmanr(dataframe_1.SalePrice,dataframe_2.SalePrice).correlation
