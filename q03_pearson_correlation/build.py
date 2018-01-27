# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here

def correlation():
    saleprice1=dataframe_1.loc[:,'SalePrice']
    saleprice2=dataframe_2.loc[:,'SalePrice']
    return float(saleprice1.corr(saleprice2))

print correlation()
