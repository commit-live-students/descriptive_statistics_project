# Default Import
import pandas as pd
import numpy as np
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

#Assign ranks to saleprice

dataframe_1['SalePriceRanked'] = dataframe_1['SalePrice'].rank(ascending=1)
dataframe_2['SalePriceRanked_2'] = dataframe_2['SalePrice'].rank(ascending=1)

#Merge both df
df_new = pd.concat([dataframe_1, dataframe_2], axis = 1)
df_new['d'] = df_new.SalePriceRanked - df_new.SalePriceRanked_2

df_new['d-squared'] = df_new['d']**2


dsqr_sum = df_new['d-squared'].sum()
sixsigma_df = 6*dsqr_sum
n = 1379
n_cube = n**3
n_diff = n_cube - n
rhs = sixsigma_df / n_diff
def spearman_correlation():
    R = 1 - rhs
    return R


spearman_correlation()
