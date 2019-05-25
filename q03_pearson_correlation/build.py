# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    #corr=dataframe_1[dataframe_1.columns[1:]].corr()['SalePrice'][:-1]
    #corr=dataframe_1['SalePrice'].corr()dataframe_2['SalePrice']
    corr1=dataframe_1['SalePrice'].corr(dataframe_2['SalePrice'])
    corr=float(corr1)
    return corr
