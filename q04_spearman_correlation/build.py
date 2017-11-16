# Default Import
import pandas as pd
import scipy.stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
rank_1 = dataframe_1['SalePrice'].rank()
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
rank_2 = dataframe_2['SalePrice'].rank()

# Your code here
def spearman_correlation():
    return scipy.stats.spearmanr(rank_1,rank_2)[0]
