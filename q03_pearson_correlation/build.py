# Default Imports
import pandas as pd
import numpy as np
dataframe_1 = pd.read_csv('./data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('./data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    sale_price_1 = dataframe_1.loc[:,'SalePrice']
    sale_price_2 = dataframe_2.loc[:,'SalePrice']
    r = np.corrcoef(sale_price_1,sale_price_2)[0,1]
    return float(r)

#print (correlation())
#print (type(correlation()))
