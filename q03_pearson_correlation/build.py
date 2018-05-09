# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    #print(dataframe_1['SalePrice'])
    #print(dataframe_2[:1])
    correlation=np.corrcoef(dataframe_1['SalePrice'],dataframe_2['SalePrice'])
    correlationt=float(correlation[0:1,1])
    return(correlationt)
   #print(type(correlationt))
#orrelation()

