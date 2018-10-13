import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    
    sale_price1 = dataframe_1.loc[:, 'SalePrice'].rank()
    sale_price2 = dataframe_2.loc[:, 'SalePrice'].rank()
    difference = (sale_price1 - sale_price2)**2
    ss = np.sum(difference)
    n = np.size(difference)
    r = 1-((6*ss)/(n*(n**2-1)))
    return r


spearman_correlation()





