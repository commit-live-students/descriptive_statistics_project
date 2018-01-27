# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
from scipy.stats import pearsonr
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    df1=dataframe_1.loc[:,'SalePrice']
    df2=dataframe_2.loc[:,'SalePrice']
    corr,p_value=pearsonr(df1,df2)
    return corr




