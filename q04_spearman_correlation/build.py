# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import scipy
import scipy.stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():    
    sale_price1 = dataframe_1.loc[:,'SalePrice']
    sale_price2 = dataframe_2.loc[:,'SalePrice']
    #then call poisson directly
    correlation_result, pvalue_result = scipy.stats.spearmanr(sale_price1,sale_price2)
    return correlation_result



