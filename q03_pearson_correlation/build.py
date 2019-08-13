import numpy as np
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def correlation():
    return float(np.corrcoef(dataframe_1['SalePrice'], dataframe_2['SalePrice'])[0,1])
