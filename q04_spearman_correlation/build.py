# Default Import
import pandas as pd
from scipy import stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here

def spearman_correlation():
    sale_price_1 = dataframe_1.loc[:,'SalePrice']
    sale_price_2 = dataframe_2.loc[:,'SalePrice']
    #print sale_price_2
    spearman = stats.spearmanr(sale_price_1,sale_price_2)
    return spearman[0]
