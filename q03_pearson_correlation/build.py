# Default Imports
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    df03 = pd.concat((dataframe_1['SalePrice'], dataframe_2['SalePrice']), axis=1, join='inner')
    return np.corrcoef(df03.ix[:,0],df03.ix[:,1])[0][1]
