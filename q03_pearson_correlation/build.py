# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

Sales_Price_1 = dataframe_1.SalePrice
Sales_Price_2 = dataframe_2.SalePrice



# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    return np.corrcoef(Sales_Price_1, Sales_Price_2)[0,1]

    

correlation()


