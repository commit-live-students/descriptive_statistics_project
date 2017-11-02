# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('/home/utk1801/Workspace/code/descriptive_statistics_project/data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('/home/utk1801/Workspace/code/descriptive_statistics_project/data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    corr1 = dataframe_1['SalePrice'].corr(dataframe_2['SalePrice'])
    return corr1
correlation()
