# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    sp1=(dataframe_1['SalePrice'].describe())
    
    sp2=(dataframe_2['SalePrice'].describe())
    
    v1=(((dataframe_1['SalePrice']-sp1['mean'])/sp1['std']))
    v2=(((dataframe_2['SalePrice']-sp2['mean'])/sp2['std']))
    z=(sum(v1*v2))
    
    r=(1/(sp2['count']-1)*z)
    return(r)
#correlation()

