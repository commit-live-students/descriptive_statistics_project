# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import scipy.stats
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
#dataframe_2.info()
def spearman_correlation():
    sale_price_1=dataframe_1['SalePrice']
    sale_price_2=dataframe_2['SalePrice']
    #print()
    corr,rank=scipy.stats.spearmanr(sale_price_1,sale_price_2)
    return corr.item()

#spearman_correlation()
#type(spearman_correlation())
