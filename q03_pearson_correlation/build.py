# Default Imports
import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    sale_price1 = dataframe_1["SalePrice"]
    sale_price2= sale_price = dataframe_2["SalePrice"]
    correl = float(np.corrcoef(sale_price1, sale_price2)[0, 1])
    #col = pearsonr(sale_price1, sale_price2)
    return correl

print correlation()
