# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here
def spearman_correlation():
    #Convert Series in DF
    sale_price_1 = dataframe_1[['SalePrice']]
    sale_price_2 = dataframe_2[['SalePrice']]

    n = sale_price_2.shape[0]
    #calculate ranks using rank function
    sale_price_1['rank_1'] = sale_price_1['SalePrice'].rank(ascending=1)
    sale_price_2['rank_2'] = sale_price_2['SalePrice'].rank(ascending=1)

    #Calculate the difference in ranks and calculate square of that diff
    d = sale_price_2['rank_2'] - sale_price_1['rank_1']
    d_squared = d**2
    d2 = d_squared.sum()  # sum the d squares

    #SRCC : Spearman Correlation Coefficient 
    p = 1 - 6*d2/(n**3 - n)
    
    return p


spearman_correlation()










