# %load q04_spearman_correlation/build.py
# Default Import
import pandas as pd
import numpy as np

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here

def spearman_correlation():
    dataframe_1['saleprice_rank'] = dataframe_1['SalePrice'].rank(ascending=True)
    dataframe_2['saleprice_rank'] = dataframe_2['SalePrice'].rank(ascending=True)
    dataframe_1['d'] = dataframe_1['saleprice_rank']-dataframe_2['saleprice_rank']
    dataframe_1['d-squared']= dataframe_1['d']*dataframe_1['d']
    spearman_cc = 1-((6*(np.sum(dataframe_1['d-squared'])))/(dataframe_1.shape[0]*((dataframe_1.shape[0]*dataframe_1.shape[0])-1)))
    return spearman_cc

    

    
    
        








