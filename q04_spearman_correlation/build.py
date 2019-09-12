# Default Import
import pandas as pd
import numpy as np
from scipy.stats import spearmanr

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Your code here

def spearman_correlation():
    sales_price1 = dataframe_1["SalePrice"]
    sales_price2 = dataframe_2["SalePrice"]
    col = spearmanr(sales_price1, b=sales_price2).correlation
    return col
print spearman_correlation()
