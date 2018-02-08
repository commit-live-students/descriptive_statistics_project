# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
df1=dataframe_1.loc[:,'SalePrice']
df2=dataframe_2.loc[:,'SalePrice']
def correlation():
    return np.corrcoef(df1,df2)[0,1]
#correlation()
#print dataframe_1


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
