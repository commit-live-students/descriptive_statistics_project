import numpy as np
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def correlation():
    sp1 = dataframe_1['SalePrice']
    sp2 = dataframe_2['SalePrice']
    pc = np.corrcoef(sp1, sp2)[0,1]
    return pc
