# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

def correlation():
    saleprice1 = dataframe_1.loc[:, "SalePrice"]
    #print(saleprice1)

    saleprice2 = dataframe_2.loc[:, "SalePrice"]
    #print(saleprice2)
    #print(dataframe_2['SalePrice'])
    x = saleprice1.corr(saleprice2)
    #print(x)
    return x



# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
