# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    sale_price_1 = dataframe_1.loc[:, 'SalePrice']
    sale_price_2 = dataframe_2.loc[:,'SalePrice']
    
    df=pd.DataFrame(sale_price_1)
    df['SalePrice2']=sale_price_2
    
    ans=df.corr(method='spearman').iloc[1,0]
    return ans

    
spearman_correlation()



