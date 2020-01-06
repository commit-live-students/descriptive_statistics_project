# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    sale1 = dataframe_1['SalePrice']
    sale2 = dataframe_2['SalePrice']
    #data = pd.concat([sale1,sale2],axis = 1)
    #co = data.corr()
    correlation = sale1.corr(sale2) #find correlation between sale1 and sale2
    return correlation

correlation()


