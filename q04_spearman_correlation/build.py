# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
from scipy.stats import spearmanr


def spearman_correlation():
    dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
    dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
    return spearmanr(dataframe_1.SalePrice,dataframe_2.SalePrice)[0]






