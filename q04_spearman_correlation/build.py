# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
def spearman_correlation():
    new_dict = {'SP1':dataframe_1['SalePrice'],'SP2':dataframe_2['SalePrice']}
    new_df=pd.DataFrame(new_dict)
    new_df['sp_rank1']=new_df['SP1'].rank(ascending=True)
    new_df['sp_rank2']=new_df['SP2'].rank(ascending=True)
    new_df['d']=new_df['sp_rank1']-new_df['sp_rank2']
    new_df['d-squared']=new_df['d']**2
    a=sum(new_df['d-squared'])
    b=len(new_df)
    x=1-(6*a/(b*(b**2-1)))
    return float(x)
