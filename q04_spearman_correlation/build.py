# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
from scipy import stats
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    
    return stats.spearmanr(dataframe_1['SalePrice'],dataframe_2['SalePrice']).correlation
     

