# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
def spearman_correlation():

    saleprice1 = dataframe_1.loc[:, "SalePrice"]
    #print(saleprice1)

    saleprice2 = dataframe_2.loc[:, "SalePrice"]
    #print(saleprice2)
    #print(dataframe_2['SalePrice'])
    x = saleprice1.corr(saleprice2, method = 'spearman')
    #print(x)
    return x
