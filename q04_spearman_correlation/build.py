# Default Import
import pandas as pd
from scipy.stats import spearmanr

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    data1 = dataframe_1['SalePrice']
    data2 = dataframe_2['SalePrice']
    data = spearmanr(data1,data2)
    return float(data.correlation)
