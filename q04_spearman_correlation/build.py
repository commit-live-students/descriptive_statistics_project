# De
import pandas as pd
import numpy as np
dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
df = pd.concat([dataframe_1["SalePrice"],dataframe_2["SalePrice"]], axis= 1)
# Your code here
def spearman_correlation():
    x = df.corr(method="spearman").iloc[0,1]
    return x

# Your code here
