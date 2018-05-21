# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    df=dataframe_1.loc[:,['SalePrice']].rank()
    df['SalePrice2']=dataframe_2.loc[:,['SalePrice']].rank()
    df['d']=df['SalePrice']-df['SalePrice2']
    df['dsq']=df['d']**2
    sum_dsq=df['dsq'].sum()
    count_dsq=df['dsq'].count()
    x = 1-((6 * sum_dsq)/(count_dsq*(count_dsq**2-1)))
    return x

#spearman_correlation()

