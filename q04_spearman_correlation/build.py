# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    df1 = DataFrame(dataframe_1, columns=['SalePrice']).sort_values('SalePrice', ascending=True)
    df2 = DataFrame(dataframe_2, columns=['SalePrice']).sort_values('SalePrice', ascending=True)
    df_merge = df1.merge(df2, left_index=True, right_index=True)
    df_coef = df_merge.corr(method='spearman')
    return df_coef.iloc[0, 1]



