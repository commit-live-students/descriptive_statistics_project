# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
#     print(dataframe_1.head())
#     print(dataframe_2.head())
    return dataframe_1['SalePrice'].corr(dataframe_2['SalePrice'],'pearson')
