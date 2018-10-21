# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    df1 = pd.DataFrame(dataframe_1['SalePrice'])
    df2 = pd.DataFrame(dataframe_2['SalePrice'])
    df3 = pd.concat([df1,df2],axis=1)
    #print(df3)
    return df3.corr(method='spearman',min_periods=1).iloc[0,1]
    
spearman_correlation()


