# Default Import
import pandas as pd
from scipy import stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

sale_price1 = dataframe_1.loc[:, 'SalePrice']
sale_price2 = dataframe_2.loc[:, 'SalePrice']


def spearman_correlation():
    return stats.spearmanr(sale_price1,sale_price2)[0]

print spearman_correlation()
