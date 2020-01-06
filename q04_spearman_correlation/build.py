# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
from scipy.stats import spearmanr

def spearman_correlation():
    dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
    dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
    v1, v2 = spearmanr(dataframe_1.iloc[:,-1],dataframe_2.iloc[:,-1])
    return v1

spearman_correlation()



