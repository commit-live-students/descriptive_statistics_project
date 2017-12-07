# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
from scipy.stats import spearmanr
def spearman_correlation():
    return spearmanr(dataframe_1['SalePrice'], dataframe_2['SalePrice']).correlation

#print spearman_correlation()
