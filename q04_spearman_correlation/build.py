# Default Import
import pandas as pd
from scipy import stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    sale_price1 = dataframe_1['SalePrice']
    sale_price2 = dataframe_2['SalePrice']
    sc = stats.spearmanr(sale_price1, sale_price2)
    return sc.correlation

spearman_correlation()
