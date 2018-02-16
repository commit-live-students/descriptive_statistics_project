# Default Imports
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    Sale_price1 = dataframe_1.loc[:,'SalePrice']
    Sale_price2 = dataframe_2.loc[:,'SalePrice']
    cr = np.corrcoef(Sale_price1, Sale_price2)[0,1]
    #return Sale_price1,Sale_price2
    #print type(cr)
    return cr

#print correlation()
