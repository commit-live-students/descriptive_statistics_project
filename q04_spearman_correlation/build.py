# Default Import
import pandas as pd
import numpy as np
from scipy.stats import spearmanr

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    a=spearmanr(dataframe_1.SalePrice,dataframe_2.SalePrice)[0]
    return a

spearman_correlation()
