# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


def correlation():
    df1= dataframe_1.loc[:,['SalePrice']]
    df2= dataframe_2.loc[:,['SalePrice']]
    return df1.corrwith(df2)['SalePrice']
# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
correlation()

