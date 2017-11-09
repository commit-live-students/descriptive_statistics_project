# Default Import
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    df = pd.concat([dataframe_1['SalePrice'], dataframe_2['SalePrice']], axis=1)
    df.columns = ['SalePrice1', 'SalePrice2']
    df['Rank1'] = np.argsort(df['SalePrice1']).sort_values().index
    df['Rank2'] = np.argsort(df['SalePrice2']).sort_values().index
    df['d'] = df['Rank1'] - df['Rank2']
    df['d-squared'] = df['d'] ** 2
    d_squared_sum = df['d-squared'].sum()
    n = df.shape[0]
    q = n * ( n ** 2 - 1 )
    sp = 1 - ((6 * d_squared_sum) / float(q))
    return sp
