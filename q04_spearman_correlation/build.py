# Default Import
import pandas as pd
import scipy.stats as st

def spearman_correlation():
    dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
    dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

    cor_spearman = st.spearmanr(dataframe_1['SalePrice'] , dataframe_2['SalePrice'])
    return cor_spearman[0]
# Your code here
spearman_correlation()
# Your code here
