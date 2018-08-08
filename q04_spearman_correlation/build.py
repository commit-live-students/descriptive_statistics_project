# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
from scipy.stats.stats import spearmanr
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def spearman_correlation():
    df1=pd.DataFrame(dataframe_1)
    df2=pd.DataFrame(dataframe_2)
    a=df1['SalePrice'].astype(float)
    b=df2['SalePrice'].astype(float)
    sc=spearmanr(a,b)
    return sc[0]
    


c=spearman_correlation()
c


