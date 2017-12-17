# Default Imports
import pandas as pd
import numpy as np
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    frame1 = dataframe_1['SalePrice']
    frame2 = dataframe_2['SalePrice']
    return float(np.corrcoef(x=frame1,y=frame2)[0,1])
