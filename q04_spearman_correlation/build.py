# Default Import
import pandas as pd
import scipy.stats as sy

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    a = dataframe_1['SalePrice']
    b = dataframe_2['SalePrice']
    #return ((a - b)**2).sum
    return float(sy.spearmanr(a,b)[0])
