# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np
import scipy.stats as st
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
def spearman_correlation():
    return st.spearmanr(dataframe_1['SalePrice'], dataframe_2['SalePrice'])[0]
