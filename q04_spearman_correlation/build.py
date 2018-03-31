# Default Import
import pandas as pd
import numpy as np
import scipy.stats as st

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    s1 = dataframe_1['SalePrice']
    s2 = dataframe_2['SalePrice']
    return float(st.spearmanr(s1,s2)[0])
