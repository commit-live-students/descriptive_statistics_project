# Default Import
import numpy as np
import pandas as pd
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here

def spearman_correlation():
    df = pd.concat([dataframe_1['SalePrice'], dataframe_2['SalePrice']], axis=1)
    df.columns = ['SalePrice1', 'SalePrice2']
    df['Rank_sp1'] = np.argsort(df['SalePrice1']).sort_values().index
    df['Rank_sp2'] = np.argsort(df['SalePrice2']).sort_values().index
    df['d'] = df['Rank_sp1'] - df['Rank_sp2']
    df['d-squared'] = df['d'] ** 2
    d_sq_sum = df['d-squared'].sum()
    n = df.shape[0]
    q = n * ( n ** 2 - 1 )
    rho = 1 - ((6 * d_sq_sum) / float(q))
    return rho
