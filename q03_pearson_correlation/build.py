# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    sale_price1=(dataframe_1['SalePrice'].describe())
    
    sale_price2=(dataframe_2['SalePrice'].describe())
    
    v1=(((dataframe_1['SalePrice']-sale_price1['mean'])/sale_price1['std']))
    v2=(((dataframe_2['SalePrice']-sale_price2['mean'])/sale_price2['std']))
    z=(sum(v1*v2))
    
    r=(1/(sale_price2['count']-1)*z)
    return(r)
correlation()

