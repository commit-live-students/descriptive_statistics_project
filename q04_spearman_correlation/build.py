# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    dataframe_1['rank'] = dataframe_1.SalePrice.rank(ascending=1)
    dataframe_2['rank'] = dataframe_2.SalePrice.rank(ascending=1)

    d = abs(dataframe_1['rank'] - dataframe_2['rank'])

    d_squared_sum = pd.DataFrame(d**2).sum()

    n = len(d)

    spear_corr_coeff = 1-((6*d_squared_sum)/(n*(n**2 - 1)) )

    return float(spear_corr_coeff)


