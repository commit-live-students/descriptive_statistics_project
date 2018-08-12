# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import scipy
from scipy.stats.stats import pearsonr
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
    
def correlation():
    df1=pd.DataFrame(dataframe_1)
    df2=pd.DataFrame(dataframe_2)
    a=df1['SalePrice'].astype(float)
    b=df2['SalePrice'].astype(float)
    pearson_coeff=pearsonr(a,b)
    a=pearson_coeff[0]
    b=pearson_coeff[1]
    return (a)
# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here


c=correlation()
c


