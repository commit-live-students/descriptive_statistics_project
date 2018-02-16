# Default Import
import pandas as pd
import scipy
from scipy.stats import spearmanr

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():


    x = dataframe_1.loc[:,'SalePrice']
    y = dataframe_2.loc[:,'SalePrice']
    #print scipy.stats.stats.rankdata(Sale_price1)
    #print scipy.stats.stats.spearmanr(Sale_price1,Sale_price2 )[0]
    #scipy.stats.mstats.spearmanr(x, y, use_ties=True)[0]
    corr_ran = spearmanr(x,y)
    print type(corr_ran[0])
    return corr_ran[0]

#print spearman_correlation()
