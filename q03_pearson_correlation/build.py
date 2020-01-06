# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
from scipy.stats import pearsonr

def correlation():
    dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
    dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
    v1, v2 = pearsonr(dataframe_1.SalePrice, dataframe_2.SalePrice)
    return v1
correlation()



