# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import scipy.stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    SP_1_rank = dataframe_1['SalePrice'].rank()
    SP_2_rank = dataframe_2['SalePrice'].rank()
    Spear_Coef = scipy.stats.spearmanr(SP_1_rank,SP_2_rank)[0]
    return Spear_Coef
