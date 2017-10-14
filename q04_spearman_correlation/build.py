# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    var1 = dataframe_1['SalePrice']
    var2 = dataframe_2['SalePrice']
    len1 = len(var1)
    rnkvar1 = var1.rank()
    rnkvar2 = var2.rank()
    d = rnkvar1 - rnkvar2
    sqaure_d = d * d
    sqaure_d_sum = sqaure_d.sum()
    spearman_cof = 1 - (6*sqaure_d_sum/(len1*len1*len1 -len1))
    return spearman_cof
