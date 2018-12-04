# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
from scipy.stats import spearmanr

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

SalesPrice_1=dataframe_1.SalePrice
SalesPrice_2=dataframe_2.SalePrice


def spearman_correlation():
    coef, p = spearmanr(SalesPrice_1, SalesPrice_2)
    return coef



spearman_correlation()


