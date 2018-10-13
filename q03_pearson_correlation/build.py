import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def correlation():
    
    sale_price1 = dataframe_1.loc[:, 'SalePrice']
    sale_price2 = dataframe_2.loc[:, 'SalePrice']
    r = np.corrcoef(sale_price1, sale_price2)[0,1]
    return r

correlation()
    



